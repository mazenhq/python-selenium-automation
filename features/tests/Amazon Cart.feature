# Created by Mazen at 5/11/2023
Feature: Amazon Cart test

  Scenario: Verify amazon Cart is empty
    Given Open amazon
    When Click on Cart icon
    Then Verify Cart is empty