
/* global validator */

/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Laravel.
 */

window._ = require('lodash');
window.Popper = require('popper.js').default;
window.$ = window.jQuery = require('jquery');

require('../../node_modules/bootstrap/dist/js/bootstrap.js');

require('../../node_modules/adminlte/dist/js/adminlte.js');
window.swal = require('../../node_modules/sweetalert2/dist/sweetalert2.js');
window.moment = require('../../node_modules/moment/moment');
require('../../node_modules/select2/dist/js/select2.full.js');
require('../../node_modules/bootstrap-datepicker/dist/js/bootstrap-datepicker.js');
require('../../node_modules/bootstrap-daterangepicker/daterangepicker.js');
require('../../node_modules/bootstrap-timepicker/js/bootstrap-timepicker.js');
require('../../node_modules/bootstrap-colorpicker/dist/js/bootstrap-colorpicker.js');
require('../../node_modules/p-loading/dist/js/p-loading.js');
require('../../node_modules/jquery-slimscroll/jquery.slimscroll.js');
require('../../node_modules/icheck/icheck.js');
window.validator = require('../../node_modules/validator/validator.js');