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
      // .when('/about', {
      //   templateUrl: 'views/about.html',
      //   controller: 'AboutCtrl'
      // })
      // .when('/detail/:id', {
      //   templateUrl: 'views/detail.html',
      //   controller: 'DetailCtrl'
      // })
      // .when('/article/:id', {
      //   templateUrl: 'views/article.html',
      //   controller: 'ArticleCtrl'
      // })
      .otherwise({
        redirectTo: '/'
      });
  }).run(function($rootScope){
      $rootScope.serverUrl = 'http://192.168.10.10/moewiki';
  });
