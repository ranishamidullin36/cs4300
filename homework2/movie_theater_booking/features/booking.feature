Feature: Movie Theater Booking
  As a user of the movie theater booking system
  I want to view movies, book seats, and check my booking history
  So that I can plan my movie visits

  Scenario: View movie listings via API
    Given there is a movie "Inception" in the system
    When I request the movie list from the API
    Then I should see "Inception" in the response

  Scenario: Book a seat via API
    Given there is a movie "Inception" in the system
    And there is an available seat "A1"
    And there is a user "testuser"
    When I book seat "A1" for movie "Inception" as "testuser"
    Then the booking should be created successfully

  Scenario: View booking history via API
    Given there is a movie "Inception" in the system
    And there is an available seat "A1"
    And there is a user "testuser"
    And "testuser" has booked seat "A1" for "Inception"
    When I request the booking list from the API
    Then I should see a booking for "testuser"

  Scenario: View movie listings page
    Given there is a movie "Inception" in the system
    When I visit the movie list page
    Then I should see "Inception" on the page

  Scenario: View seat booking page
    Given there is a movie "Inception" in the system
    And there is an available seat "B2"
    When I visit the seat booking page for "Inception"
    Then I should see the booking form
    And I should see seat "B2" as available
