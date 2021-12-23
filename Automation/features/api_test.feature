@api
Feature: This is an XCNT graphQL api automation
  Basic scenarios will be covered like creation, deletion, updation and verification of the user

  Scenario: Create a user with random set of data and verify it
    Given Create a user through API with random data
    Then Fetch the details of the user and verify
    And Delete the user

  Scenario Outline: Create a user, update the same user and verify it
    Given Create a user firstname: <firstName>, lastname: <lastName>, email:<email> and newsletter as <newsletter>
    Then Fetch the details of the user and verify
    And Update the user firstname <updateFirsName>, lastname <updateLastName>, email <updateEmail> and newsletter <updateNewsletter>
    Then Fetch the details of the user and verify

    Examples:
      | firstName | lastName | email         | newsletter | updateFirsName | updateLastName | updateEmail      | updateNewsletter |
      | neha      | birajdar | neha@xcnt.com | true       | sandeep        | rathor         | sandeep@gmail.in | false            |

  Scenario Outline: Create multiple user and delete them in one go
    Given Create a user firstname: <firstName>, lastname: <lastName> email:<email> and newsletter as <newsletter>
    Then Delete all the previous created user

    Examples:
      | firstName | lastName | email            | newsletter |
      | sample1   | surname1 | sample1@xcnt.com | true       |
      | sample2   | surname2 | sample2@xcnt.com | true       |
      | sample3   | surname3 | sample3@xcnt.com | false      |
      | sample4   | surname4 | sample4@xcnt.com | false      |
      | sample5   | surname5 | sample5@xcnt.com | true       |
      | sample6   | surname6 | sample6@xcnt.com | false      |
      | sample7   | surname7 | sample7@xcnt.com | true       |

  Scenario Outline: Verify user should not be able to create different data with same mail id
    Given Create a user with different <firstName>, <lastName> and <newsletter> but with same <email>
    Then Verify only one user should be present if same emails are being used
    Examples:
      | firstName | lastName | email            | newsletter |
      | John      | Lane     | company@xcnt.com | true       |
      | Tina      | Joseph   | company@xcnt.com | false      |

