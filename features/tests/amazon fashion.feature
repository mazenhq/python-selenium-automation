# Created by Mazen at 6/21/2023
Feature: Verify the New arrivals for amazon fashion
  # Enter feature description here

  Scenario: Verify that user can search in a department
    Given Open amazon Fashion
    When Select department fashion
    When Hover over New arrivals
    Then Verify user sees the deals
