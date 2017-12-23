$(function () {
    $("input[name='userid']").val("");
    $("input[name='username']").val("");
    $("input[name='password']").val("");
    $("input[name='re-password']").val("");
});
$("input[type='button']").click(function (){
    var userid = $("#userid").val(); //获取
    var username = $("#username").val();
    var password = $("#password").val();
    var repassword = $("#re-password").val();
        if (userid === "" || userid === undefined || userid === null) {
             swal({
                    title:"请填写学号/工号",
                    text:"请填写完整信息！",
                    type:"warning"

                })
        } else if(username ==="" || username ===undefined || username === null){
            swal({
                    title:"请填写姓名",
                    text:"请填写完整信息！",
                    type:"warning"

                })
        }else if (password === "" || password === undefined || password === null){
            swal({
                    title:"请填写您的密码",
                    text:"请填写完整信息！",
                    type:"warning"
                })
        }else if (repassword === "" || repassword === undefined || repassword === null){
            swal({
                    title:"请再次填写您的密码",
                    text:"请填写完整信息！",
                    type:"warning"
                })
        }else if (password !== repassword){
            swal({
                    title:"两次密码不一致",
                    text:"请仔细确认密码！",
                    type:"warning"
                })
        }else {
            if($("#userid").val() != "" && $("#password").val() != "" &&$("#username").val() != ""&&$("#re-password").val() != ""){
                    $.post("sign-up", {
                        userid : $("#userid").val(), //获取
                        username : $("#username").val(),
                        password : $("#password").val(),
                        repassword : $("#re-password").val()
                    }, function (result) {
                        result = JSON.parse(result);
                        if (result["status"] === 0) {
                            alert(result["message"]);
                            window.location.reload();
                        } else if (result["status"] === 1) {
                            alert(result["message"]);
                            window.location.href =  '/teaManaSys/sign-in'
                        } else {
                            alert('服务器异常');
                            window.location.reload()
                        }
                    });
                }
        }
    });