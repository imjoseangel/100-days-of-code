Feature: configure-ssl-security command

  Background: Ensure IWF setup and we are operating the desired server
    Given we have IWF installed
    And we are operating "server00"

  Scenario: execute the configure-ssl-security command with --pfxFile
    When we invoke the configure-ssl-security command with "--pfxFile" and values
      |pfx_file           |cert_alias                        |
      |/tmp/iwf-dev.pfx   |iwf development certificate alias |

    Then security.properties is updated
    And the new certificate works
