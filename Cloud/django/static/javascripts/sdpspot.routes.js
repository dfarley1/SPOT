(function () {
	'use strict';

	angular
		.module('sdpspot.routes')
		.config(config);

	config.$inject = ['$routeProvider'];

	/**
	* @name config
	* @desc Define valid application routes
	*/
	function config($routeProvider) {
		$routeProvider.when('/register', {
			controller: 'RegisterController', 
			controllerAs: 'vm',
			templateUrl: '/static/templates/authentication/register.html'
		}).when('/login', {
			controller: 'LoginController',
			controllerAs: 'vm',
			templateUrl: '/static/templates/authentication/login.html'
		}).when('/home', {
			controller: 'MapController',
			controllerAs: 'vm',
			templateUrl: '/static/templates/home.html'
		}).otherwise('/');
	}
})();