<?php
/**
 * books.sektor9.dev - live book library index.
 * Scans the downloads dir, parses metadata from filenames, returns JSON.
 * GET /api/books.php -> full index
 * GET /api/books.php?q=linux&cat=magazine&sort=size&dir=desc -> filtered/sorted
 */
header('Content-Type: application/json; charset=utf-8');

$DL = getenv('BOOKS_DIR') ?: '/srv/books/downloads';
$files = glob($DL . '/*.*');

$books = [];
foreach ($files as $f) {
    $base = basename($f);
    if (str_starts_with($base, '.')) continue;
    $name = pathinfo($base, PATHINFO_FILENAME);
    $ext  = strtolower(pathinfo($base, PATHINFO_EXTENSION));
    if (!in_array($ext, ['pdf','epub','djvu','txt','mobi','azw3','cbz','cbr'])) continue;
    $size = filesize($f);
    $mtime = filemtime($f);

    $books[] = [
        'file'  => $base,
        'name'  => $name,
        'ext'   => $ext,
        'size'  => $size,
        'size_mb' => round($size / 1048576, 1),
        'mtime' => $mtime,
        'date'  => parseDate($name),
        'cat'   => categorize($name),
        'difficulty' => difficulty($name),
    ];
}

// query params
$q = strtolower($_GET['q'] ?? '');
$cat = $_GET['cat'] ?? '';
$sort = $_GET['sort'] ?? 'name';
$dir = $_GET['dir'] ?? 'asc';

if ($q) {
    $books = array_values(array_filter($books, function ($b) use ($q) {
        return str_contains(strtolower($b['name']), $q)
            || str_contains(strtolower($b['cat']), $q)
            || str_contains(strtolower($b['file']), $q);
    }));
}
if ($cat && $cat !== 'all') {
    $books = array_values(array_filter($books, fn($b) => $b['cat'] === $cat));
}

usort($books, function ($a, $b) use ($sort, $dir) {
    $cmp = 0;
    if ($sort === 'size') $cmp = $a['size'] <=> $b['size'];
    elseif ($sort === 'date') $cmp = ($a['date'] ?? '') <=> ($b['date'] ?? '');
    elseif ($sort === 'name') $cmp = strcmp($a['name'], $b['name']);
    elseif ($sort === 'mtime') $cmp = $a['mtime'] <=> $b['mtime'];
    return $dir === 'desc' ? -$cmp : $cmp;
});

$cats = [];
foreach ($books as $b) $cats[$b['cat']] = ($cats[$b['cat']] ?? 0) + 1;

echo json_encode([
    'total' => count($books),
    'categories' => $cats,
    'books' => $books,
], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);

function parseDate($name) {
    // patterns: 1980_06, 1984_04, 1989_09_28, 1988_Oct, Feb_1982, 1979_02
    if (preg_match('/(19|20)(\d{2})[-_](\d{1,2})(?:[-_](\d{1,2}))?/', $name, $m)) {
        $y = $m[1].$m[2]; $mo = str_pad($m[3], 2, '0', STR_PAD_LEFT);
        $d = isset($m[4]) ? str_pad($m[4], 2, '0', STR_PAD_LEFT) : '01';
        return "$y-$mo-$d";
    }
    if (preg_match('/(19|20)(\d{2})[-_](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/i', $name, $m)) {
        $mon = ['Jan'=>'01','Feb'=>'02','Mar'=>'03','Apr'=>'04','May'=>'05','Jun'=>'06','Jul'=>'07','Aug'=>'08','Sep'=>'09','Oct'=>'10','Nov'=>'11','Dec'=>'12'];
        return $m[1].$m[2]."-".$mon[$m[3]]."-01";
    }
    if (preg_match('/(19|20)(\d{2})/', $name, $m)) {
        return $m[1].$m[2]."-01-01";
    }
    return null;
}

function categorize($name) {
    $n = strtolower($name);
    $magazines = ['byte','dr_dobbs','dobb','creative_computing','compute','computing','magazine','magpi','hackspace','raspberry','retro','nibble','family_computing','micro','electronic','electron','elektor','amateur_radio','radio','qst','ham','coco','run_','ahoy','antic','analog','compute!','pc_mag','pcmag','infoworld','edn','electronics_world','electrical','wireless','popular_electronics','electronics_australia','maplin','microcomputer','softalk','hardcore','cgan','digest','journal','proceedings','review','bulletin','gazette','transactions'];
    $os = ['linux','windows','dos','unix','bsd','solaris','aix','macos','os2','vms','cp/m','vax','os/2','windows_nt','ms-dos','pcdos','command_line','powershell','bash','shell_script','shell','sed_awk','grep','vim','tmux'];
    $lang = ['c_programming','c++','cpp','python','java','javascript','rust','go_','golang','assembly','asm','fortran','cobol','pascal','basic','lisp','scheme','haskell','perl','ruby','swift','kotlin','c#','dotnet','.net','sql','php','typescript','ada','forth','prolog','smalltalk','visual_basic','vb6','vba'];
    $hw = ['arduino','esp32','esp8266','raspberry_pi','rpi','stm32','avr','pic_','msp430','fpga','verilog','vhdl','8051','8086','8085','6502','z80','68000','m68k','arm_','risc-v','riscv','x86','microcontroller','embedded','atmel','breadboard','circuit','pcb','schematic','solder','op-amp','opamp','transistor','diode','ic_','cmos','ttl','logic_gate','amplifier','oscillator','filter'];
    $kernel = ['kernel','operating_system','operating-systems','os_dev','osdev','bootloader','booting','multitasking','scheduler','memory_management','virtual_memory','paging','file_system','filesystem','driver','device_driver','interrupt','syscall','system_call','process_management','concurrency','thread','posix','system_programming','compiler','assembler','linker','loader','gnu','toolchain','qemu','x86_64','system_software'];
    $net = ['network','networking','tcp/ip','tcp_ip','internet','protocol','socket','http','dns','dhcp','router','switch','ethernet','wifi','wifi','ble','bluetooth','mqtt','iot','security','crypto','encryption','firewall','penetration','hacking','cyber'];
    $math = ['math','calculus','linear_algebra','algebra','geometry','probability','statistics','discrete','logic','number_theory','graph_theory','algorithm','data_structure'];

    foreach ($magazines as $m) if (str_contains($n, $m)) return 'Magazine';
    foreach ($math as $m) if (str_contains($n, $m)) return 'Math';
    foreach ($os as $o) if (str_contains($n, $o)) return 'Operating Systems';
    foreach ($kernel as $k) if (str_contains($n, $k)) return 'OS Dev / Kernel';
    foreach ($lang as $l) if (str_contains($n, $l)) return 'Programming Language';
    foreach ($hw as $h) if (str_contains($n, $h)) return 'Hardware / Electronics';
    foreach ($net as $nn) if (str_contains($n, $nn)) return 'Networking / Security';
    return 'General / Other';
}

function difficulty($name) {
    $n = strtolower($name);
    $hard = ['kernel','bootloader','compiler','assembler','os_dev','osdev','architecture','microcode','interrupt','memory_management','virtual_memory','paging','scheduler','multitasking','device_driver','linker','loader','advanced','internals','source_code','debugging','reverse'];
    $mid  = ['programming','language','tutorial','guide','reference','manual','handbook','introduction','embedded','microcontroller','networking','security','algorithm','data_structure','operating_system','system_programming','concurrency'];
    $beg  = ['beginner','basics','fundamentals','easy','first','learning','learn','introduction_to','starter','101','for_dummies','dummies','crash_course'];
    foreach ($beg as $b) if (str_contains($n, $b)) return 'Beginner';
    foreach ($hard as $h) if (str_contains($n, $h)) return 'Hard';
    foreach ($mid as $m) if (str_contains($n, $m)) return 'Intermediate';
    return 'Mixed';
}
