s1 = """print "Hello,World!";"""
s2 = "00000000"


## test
$string1 = 'print "Hello,World!";';
$string2 = '000O0MM00110K000M0MMM';
$result = $string1 ^ $string2;

// 結果を表示するために、各文字をASCIIコードに変換
echo "XOR result: ";
for ($i = 0; $i < strlen($result); $i++) {
    echo ord($result[$i]) . ' ';
}
echo "\n";
var_dump($result);
print '000O0MM00110K000M0MMM' ^ '@BY!DmoxU]]_gg_B!Tlov';


## system('cat flag.txt')
$string1 = "system('cat flag.txt');";
$string2 = '101000MM100M0100L000MMM';
$result = $string1 ^ $string2;

print $result;
print '101000MM100M0100L000MMM' ^ 'BIBDU]ejRQDmV]QWbDHDjdv';

## system('ls')
$string1 = "system('ls');";
$string2 = '101000MM11MMM';
$result = $string1 ^ $string2;

print $result;
print '101000MM10MMM' ^ 'BIBDU]ej]Bjdv';

##
$string1 = '$d=file_get_contents(\'flag.txt\');echo $d;';
$string2 = 'M0M00100000012100101MM0M00L000MMM0100MM0M';
$result = $string1 ^ $string2;

print $result;
print 'M0M00100000012100101MM0M00L000MMM0100MM0M' ^ 'iTpVY]UoWUDoR]_DU_DBejV!QWbDHDjdvURX_miTv';


#
$string1 = '$d=file_get_contents(\'flag.txt\');print $d;';
$string2 = 'M0M00100000012100101MM0M00L000MML1010MMMMM';
$result = $string1 ^ $string2;

print $result;
print 'M0M00100000012100101MM0M00L000MML1010MMMMM' ^ 'iTpVY]UoWUDoR]_DU_DBejV!QWbDHDjdwABX^9mi)v';

#
$string1 = '$d=file_get_contents(\'flag.txt\');print $d;';
$string2 = 'M0M00100000012100101MM0M00L000MML2010MMMMM';
$result = $string1 ^ $string2;

print $result;
print 'M0M00100000012100101MM0M00L000MML2010MMMMM' ^ 'iTpVY]UoWUDoR]_DU_DBejV!QWbDHDjdwBBX^9mi)v';

##
$l=file('0100L000' ^ 'V]QWbDHD');print_r($l);
