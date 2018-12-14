@retrieve_location
Feature: Retrieve location

  Background:
    Given the endpoint is "https://pizza.de/dowant-api/locations/"

  @retrieve_city_info
  Scenario Outline: Retrieve city info
    When I send GET request with "<City>" parameter
    Then I should see status code is 200
    And I should see the response is not empty
    And I should see "data" field in the response
    And I should see "pagination" field in the response


  Examples:
    |City              |
    |Berlin            |
    |Neuhardenberg     |
    |München           |
    |Kirchheimbolanden |