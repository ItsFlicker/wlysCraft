function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    }


var zssr = document.getElementById("zssr");
var zsjg = document.getElementById("zsjg");

zssr.addEventListener("input", zspd);

function zspd()
{
    var zs = parseInt(zssr.value);
    if (isNaN(zs)){
        zsjg.innerHTML = "";
        return false;
    }
    if (zs < 2){
        zsjg.innerHTML = "结果:" + zs + "不是一个有效数字!(请输入大于1的整数)";
        return false;
    }

    if (zs < 4){
        zsjg.innerHTML = "结果:" + zs + "是一个质数!";
        return true;
    }
    for (var a = 2;a <= zs / 2;a++)
    {
        if (zs % a === 0)
        {
            zsjg.innerHTML = "结果:" + zs + "是一个合数!" + "\n" + "它的因数除了1和它本身还有" + a + "!";
            return true;
        }
    }

    zsjg.innerHTML = "结果:" + zs + "是一个质数!";
    return true;
}

var qrtext = document.getElementById("qrtext");
var qrsubmit = document.getElementById("qrsubmit");
var qrwindow = document.getElementById("qrwindow");

function updateQR() {
    qrwindow["src"] = "https://cli.im/api/qrcode/code?text=" + qrtext.value;
    qrwindow.className = null;
}

qrsubmit.addEventListener("click", updateQR);

qrtext.addEventListener("keypress", qrKeypress);

function qrKeypress(event) {
    if(event.which === 13) {
        updateQR.call();
    }
}
jQuery.support.cors = true;
$(function () {
    function getfanyi() {
        var content = document.getElementById('fanyitext').value;
        var tk = TL(content);
        var params = {
            tk: tk,
            q: content,
        };
        $.ajax({
            type: 'GET',
            url: "https://translate.google.cn/translate_a/single?client=t&sl=auto&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2",
            data: params,
            success: function (result) {
                $("#fanyiresult").html("翻译结果"+result);
            },
            error: function () {
                alert("翻译失败，请稍后再试");
                alert("错误代码:"+tk);
            }
        })
    }
    $("#fanyisubmit").on("click", getfanyi)
});

$(function () {
    var $bdfile = $("#bdfile");
    var $bdshow = $("#bdshow");
    var $bdupload = $("#bdupload");
    var $bdinfo = $("#bdinfo");
    var $bdresult = $("#bdresult");
    var $bdbar = $("#bd")

    $bdupload.on("click", bdupload);

    function bdupload() {
        var fs = $bdfile[0].files[0];

        if ($bdfile.val() === "") {
            alert("请选择文件！");
            return false;
        }
        var filesize = fs.size;
        if (filesize > 1024 * 1024 * 100) {
            alert("请上传小于100MB的文件！");
            return false;
        }

        $bdfile.hide();
        $bdupload.hide();

        $(".progress").show();

        var xhr = new XMLHttpRequest();
        xhr.open('post', "https://s.threatbook.cn/api/v2/file/upload", true);

        xhr.onreadystatechange=function (){
        //readystate为4表示请求已完成并就绪
            if(this.readyState===4){
                result = JSON.parse(this.response);
                if(result.response_code === 0){
                    $(".progress").hide();
                    $bdresult.hide();
                    $bdshow.css("display", "unset");
                    $bdshow.attr("src", result.permalink);
                }
                else{
                    $bdfile.show();
                    $bdupload.show();
                    $(".progress").hide();
                    $bdresult.hide();
                    alert("错误代码:", result.msg);
                    return false;
                }
            }
        };

        xhr.upload.onprogress=function (ev){
            if(ev.lengthComputable){
                var precent=100 * ev.loaded/ev.total;
                $bdinfo.css("width", precent+'%');
                $bdresult.text(Math.floor(precent)+'%');
            }
        };

            var formData = new FormData();
            formData.append("file", fs);
            formData.append("apikey", "121c1cebba784212ae641e0e6ea86fff301baeb43adb4248b3def52eff102f24");
            formData.append("run_time", 120);
            formData.append("sandbox_type", "win7_sp1_enx86_office2013");

            xhr.send(formData)
    }
});
