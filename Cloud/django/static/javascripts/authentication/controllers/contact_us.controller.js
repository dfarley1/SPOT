/**
* ContactUsController
* @namespace sdpspot.authentication.controllers
*/
(function () {
	'use strict';

	angular
		.module('sdpspot.authentication.controllers')
		.controller('ContactUsController', ContactUsController);

	ContactUsController.$inject = ['$location', '$scope', 'Authentication', 'ngDialog'];

	/**
	* @namespace ContactUsController
	*/
	function ContactUsController($location, $scope, Authentication, ngDialog) {
		var c = this;
		c.contactus = contactus;
		
        function contactus() {
        ngDialog.open({ template: 'contact_us.html', className: 'ngdialog-theme-default' });  
        };
	}
})();