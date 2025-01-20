import "hash"
rule shengtian_html
{
    meta:
        description="样本伪造成html"
        author = "pocosin"
        date = "20250117"
    strings:
        $name = "http://23.248.217.155:6311/154.207.55.200_86.bin"
    condition:
        $name or hash.md5(0,filesize)=="ab3c9822edbf732e21e5e06687014acb"
}
