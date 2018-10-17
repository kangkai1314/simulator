/**
 * Created by Administrator on 2018/10/16.
 */
$(document).ready(function() {
    $("#cancel").click(function () {
        $.ajax({
            url: "regress/tasks/",
            type: 'get',

            success: function (data, status) {
                console.log(data)

            }
        })
    })
})
