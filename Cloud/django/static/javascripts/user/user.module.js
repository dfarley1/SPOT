(function () {
    'use strict';

    angular
        .module('sdpspot.user', [
            'sdpspot.user.controllers',
            'sdpspot.user.services'
        ]);

    angular
        .module('sdpspot.user.controllers', []);

    angular
        .module('sdpspot.user.services', ['ngCookies']);
})(); 
