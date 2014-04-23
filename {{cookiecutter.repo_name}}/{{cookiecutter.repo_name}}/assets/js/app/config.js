'use strict';

//Setting up route
angular.module('{{cookiecutter.project_name}}').config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

  $urlRouterProvider.otherwise('/'); // if no route matches, redirect here

  // How to use stateProvider's ui-router: https://github.com/angular-ui/ui-router/wiki
  $stateProvider
    .state('home', {
      url: '/',
      templateUrl: '../../../templates/partials/index.html'
    })

    // add other states here

}]);