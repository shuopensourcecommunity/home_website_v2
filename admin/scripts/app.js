'use strict';
/**
 * @ngdoc overview
 * @name oscApp
 * @description
 * # oscApp
 *
 * Main module of the application.
 */
angular
.module('oscApp', [
		'ngRoute'
		])
.config(function ($routeProvider) {
	$routeProvider
	.when('/', {
		templateUrl: 'views/main.html',
		controller: 'MainCtrl'
	})
.when('/login',{
	templateUrl: 'views/login.html',
	controller: 'LoginCtrl'
})
.otherwise({
	redirectTo: '/'
});
}).run(function($rootScope){
	$rootScope.serverUrl = 'http://192.168.10.10/moewiki';
});
