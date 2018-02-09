function init() {
    anstypes = {
        'type=1':'chongding',
        'type=2':'jinri',
        'type=3':'baidu',
        'type=4':'youku',
        'type=5':'zhihu',
        'type=6':'uccry',
        'type=7':'mogujie',
        'type=8':'ireader',
        'type=9':'yingke',
        'type=10':'douyu',
        'type=11':'ucpp',
        'type=12':'biyao',
        'type=13':'bobo',
        'type=14':'jidong',
        'type=15':'geinihua',
        'type=16':'tengxun',
        'type=17':'weibo',
        'type=18':'qianfan',
    }

    var atype = document.getElementById("chongding");
    var url = location.href;
    var arg = url.match(/type=\d+/);
    if(arg != undefined) {
        arg = arg[0];
        for(var k in anstypes) {
            if(k == arg) {
                atype = document.getElementById(anstypes[k]);
                break;
            }
        }
    }
    
    if(atype != undefined) {
        var st = $('.anstype');
        for(var i=0; i<st.length; i++) {
            //if(st[i].checked == true) 
            {
                st[i].checked = false;
                $(st[i]).removeAttr("selected");
                break;
            }
        }
        atype.checked = true;
        $(atype).attr("selected", "selected");
    } 
    var search = document.getElementById("sbaidu");
    if(url.indexOf("search=1") != -1) {
        search = document.getElementById("sbaidu");
    }
    else if(url.indexOf("search=2") != -1) {
        search = document.getElementById("mbaidu");
    }
    else if(url.indexOf("search=3") != -1) {
        search = document.getElementById("sogou");
    }
    else if(url.indexOf("search=4") != -1) {
        search = document.getElementById("google");
    }
    else if(url.indexOf("search=5") != -1) {
        search = document.getElementById("bing");
    }
    else if(url.indexOf("search=6") != -1) {
        search = document.getElementById("s360");
    }
    if(search != undefined) {
        search.checked = true;
    }
    if(url.indexOf("localcap") != -1) {
        $("#localcap").attr("checked", "checked");
        $("#localocr").removeAttr("disabled");
        if(url.indexOf("tess") != -1) {
            $("#localocr").attr("checked", "checked");
        }
    }
    if(url.indexOf("delno=1") == -1) {
        $("#delno").removeAttr("checked");
    }
    if(url.indexOf("addans=1") != -1) {
        $("#addans").attr("checked", "checked");
    }
}

function searchtype() {
    var st = $('.stype');
    for(var i=0; i<st.length; i++) {
        if(st[i].checked == true) {
            return $(st[i]).val();
        }
    }
    return '';
}

function answertype() {
    // var st = $('.anstype');
    // for(var i=0; i<st.length; i++) {
    //     if(st[i].checked == true) {
    //         return $(st[i]).val();
    //     }
    // }
    return $("#atype")[0].value;
}

function presubmit() {
    //本版本默认本地功能
    if(answertype() == "") {
        $("#question").html('选择要答题的平台');
        return false;
    }
    if(searchtype() == "") {
        $("#question").html('选择你需要的搜索引擎');
        return false;
    }
    var localcap = document.getElementById("localcap");
    var localocr = document.getElementById("localocr");
    if(localcap.checked) {
        // $.get('http://localhost:9880/screencap', 
        //     function(data){
        //         console.log("1111");
        //         //document.write(data);
        //   }, 'jsonp')
        var url = 'http://localhost:9880/screencap/?type='+answertype()+'&search='+searchtype();
        if(localocr.checked) {
            var delno = $("#delno")[0].checked ? "1":"";
            var addans = $("#addans")[0].checked ? "1":"";
            url = 'http://localhost:9880/screencap/?tess=1&type='+answertype()+'&search='+searchtype()+'&delno='+delno+'&addans='+addans;;
        }
        $.ajax({
            url: url,
            //data: data,
            dataType: 'JSONP',
            success: function(data) {
                var data1 = data.data;
                if(data1.substr(0, 4) == "ERR:") {
                    var td = $("#questionans td");
                    for(var i =0; i<td.length; i++) {
                        $(td).html("")
                    }
                    $("#question").html(data1);
                    $("#questionans tr:eq(1) td:eq(0)").html("请检查AnswerotX配置是否正确");
                } else {
                    // $.post({
                    //     url: '/search/?type='+answertype()+'&search='+searchtype(),
                    //     data: encodeURIComponent(data.data),//base64 /+=符号丢失
                    //     success: function(data) {
                    //         location.href = location.href + '?type='+answertype()+'&search='+searchtype();
                    //         console.log(location.href);
                    //         //document.write(data);
                    //     }
                    // })
                    var action = localocr.checked ? '/search/?tess=1&localcap=1&type='+answertype()+'&search='+searchtype() : '/search/?localcap=1&type='+answertype()+'&search='+searchtype()
                    if(localocr.checked) {
                        data1 = Base64.decode(data1);
                        data1 = JSON.parse(data1);

                        $("#questionans").html("");

                        var innerhtml = '<tr><td id="question" colspan="3" style="font-weight:bold">'+data1.question+' <br/></td></tr>';
                        for(var i =0; i<data1.count; i++) {
                            var a = data1.answert[i].ans;
                            var c = data1.answert[i].count;
                            var tmp = '<tr>';
                            tmp = tmp + '<td name="answer" style="color:red;text-indent: 20px;font-weight:bold">'+a+'</td>';
                            tmp = tmp + '<td style="color:red;font-weight:bold">'+c+'</td>';
                            tmp = tmp + '<td>';
                            tmp = tmp + '<a class="secsearch" href="#" onclick="return secsearch(\''+a+'\');">搜</a> ';
                            tmp = tmp + '<a class="secsearch" href="#"  onclick="return secsearch(\''+a+'\', \''+data1.question+'\');">加问搜</a>';
                            tmp = tmp + '</td>';
                            tmp = tmp + '</tr>';
                            innerhtml = innerhtml + tmp;
                        }
                        $("#questionans").html(innerhtml);
                        $("#resultfrm").attr("src", "http://localhost:9880/result/");
                    } else {
                        var delno = $("#delno")[0].checked ? "1":"";
                        var addans = $("#addans")[0].checked ? "1":"";
                        action = action + '&delno='+delno+'&addans='+addans;
                        $("#search_ans").attr("action", action);
                        $("#search_data").val(encodeURIComponent(data1));//base64 /+=符号丢失
                        $("#search_ans").submit();
                    }
                   
                }
            },
            error: function(xhr, msg) {
                var td = $("#questionans td");
                for(var i =0; i<td.length; i++) {
                    $(td).html("")
                }
                $("#question").html("ERR: 请求AnswerotX失败");
                $("#questionans tr:eq(1) td:eq(0)").html("请检查AnswerotX是否正常启动");
            }
            });
        return false;
    }
    return true;
}
function secsearch(key, question) {
    var smap = {
        "1": "http://www.baidu.com/s?wd=",
        "2": "https://m.baidu.com/s?word=",
        "3": "https://www.sogou.com/sgo?query=",
        "4": "https://www.google.com/search?q=",
        "5": "http://cn.bing.com/search?go=搜索&qs=ds&form=QBRE&q=",
        "6": "https://www.so.com/s?q=",
    }
    var st = $('input.stype');
    for(var i=0; i<st.length; i++) {
        if(st[i].checked == true) {
            var url = smap[$(st[i]).val()];
            console.log(url);
            if(question != undefined) {
                key = question + ' ' + key;
            }
            window.open(url+key, "__blank");
            break;
        }
    }
    
    return false;
}

function tess_switch() {
    var localcap = document.getElementById("localcap");
    if(localcap.checked) {
        $("#localocr").removeAttr("disabled");
    } else {
        $("#localocr").attr("disabled", "disabled");
    }
}
function tess_check() {
    var localcap = document.getElementById("localcap");
    var localocr = document.getElementById("localocr");
    if(localocr.checked && !localcap.checked) {
        localocr.checked = false;
        return false;
    }
}

function switch_detail() 
{
    if($("detail").checked) {

    } 

    $("#left").toggleClass("col-md-12");
    $("#left").toggleClass("col-md-4");
    $("#right").toggleClass("col-md-8");
    $("#right").toggleClass("column");
    $("#resultfrm").toggleClass("hidden");
}

$(document).ready(function(){
    init();
    current_version();
    check_update();
    get_annouce();
});

function check_update() {
    if($("#newversion")[0] != undefined) {
        $.get('https://raw.githubusercontent.com/anhkgg/answerot/master/VERSION', 
            function(data){
                $("#newversion").html(data);
        })
    }
}

function get_annouce()
{
    if($("#annouce")[0] != undefined) {
        $.get('https://raw.githubusercontent.com/anhkgg/answerot/master/ANNOUNCE', 
        function(data){
            $("#annouce").html(data);
            show_annouce();
        })
    }
}

function current_version() 
{
    var VERSION = '0.1.8';
    var obj = $(".VERSION");
    for(var i=0; i<obj.length; i++) {
        $(obj[i]).html(VERSION);
    }
}

function show_annouce() 
{
    var num = 50;
    function goLeft() {
        //750是根据你给的尺寸，可变的
        if (num == -750) {
            num = 0;
        }
        num -= 1;
        $(".scroll").css("margin-left", num);
    }
    //设置滚动速度
    var timer = setInterval(goLeft, 40);
    //设置鼠标经过时滚动停止
    $(".box").hover(function() {
            clearInterval(timer);
        },
        function() {
        timer = setInterval(goLeft, 40);
    })
}