import "hash"
rule   md5_msi_bypass_kapa
{
    meta:
        description = "该样本卡巴斯基免杀"
        author = "pocosin"
        date = "20250116"
    //strings:
        //
    condition:
        hash.md5(0,filesize)=="6db64a320741d95237bd74b3dd6a5232"
}
