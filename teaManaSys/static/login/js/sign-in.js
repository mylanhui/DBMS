$(function () {
    $("input[name='userid']").val("");
    $("input[name='password']").val("");
});
$("input[type='button']").click(function (){
    var userid = $("#userid").val(); //获取
    var password = $("#password").val();
        if (userid === "" || userid === undefined || userid === null) {
            if (password === "" || password === undefined || password === null) {

                swal({
                    title:"请账号和密码",
                    text:"请填写完整信息！",
                    type:"warning"

                })
            } else {
                swal({
                    title:"请输入账号",
                    text:"请填写完整信息！",
                    type:"warning"
                })
            }
        } else {
            if (password === "" || password === undefined || password === null) {

                swal({
                    title:"请输入密码",
                    text:"请填写完整信息！",
                    type:"warning"
                })
            } else {
                if($("#userid").val() != "" && $("#password").val() != ""){
                    $.post("sign-in", {
                        "userid": $("input[name='userid']").val(),
                        "password": $("input[name='password']").val(),
                    }, function (result) {
                        result = JSON.parse(result);
                        if (result["status"] === 0) {
                            alert(result["message"]);
                            window.location.reload();
                        } else if (result["status"] === 1) {
                            alert(result["message"]);
                            window.location.href =  '/teaManaSys/courses'
                        } else {
                            alert('服务器异常');
                            window.location.reload()
                        }
                    });
                }
            }
        }
    });
