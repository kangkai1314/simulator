/**
 * Created by Administrator on 2018/10/11.
 */

$.noConflict();
jQuery(document).ready(function() {
    jQuery("p").click(function () {
        jQuery(this).hide();
    });
    jQuery("button").click(function () {
        jQuery("#project").fadeIn();

    });
});







