'use strict';

/* jasmine specs for controllers go here */

describe('controllers', function(){
  beforeEach(module('{{ cookiecutter.project_name }}.controllers'));


  it('should ....', inject(function($controller) {
    //spec body
    var indexCtrl = $controller('IndexController');
    expect(indexCtrl).toBeDefined();
  }));
});
