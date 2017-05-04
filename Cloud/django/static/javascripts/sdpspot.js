(function () {
	'use strict';

	angular
		.module('sdpspot', [
			'sdpspot.config',
			'sdpspot.routes',
			'sdpspot.authentication',
			'sdpspot.layout',
      'sdpspot.monitor'
		]);

	angular
		.module('sdpspot.routes', ['ngRoute']);
	
	angular
		.module('sdpspot.config', []);
	
	angular
		.module('sdpspot')
		.run(run);

	run.$inject = ['$http'];

	/**
	* @name run
	* @desc Update xsrf $http headers to align with Django's defaults
	*/
	function run($http) {
		$http.defaults.xsrfHeaderName = 'X-CSRFToken';
		$http.defaults.xsrfCookieName = 'csrftoken';
	}
})();
