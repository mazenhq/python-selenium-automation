# Created by Mazen at 6/17/2023
Feature: Verify user can search in a department


  Scenario: Verify that user can search in a department
    Given Open amazon page
    When Select department computers
    When Input PC into search amazon field
    Then Verify correct computers department shown by the url


