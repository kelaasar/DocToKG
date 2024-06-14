import requests

url = 'http://NPI3EEC39:7200/repositories/myrepo1'

headers = {
    'Content-Type': 'application/rdf+xml',
    'Accept': 'text/plain'
}

data = '''
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns="http://example.org/ns#">

<!-- Individuals -->
<rdf:Description rdf:about="#thisDirective">
  <rdf:type rdf:resource="#Directive"/>
  <defines rdf:resource="#managingAndOverseeingNASAsNuclearFlightSafetyActivities"/>
  <provides rdf:resource="#theRequirements"/>
  <describes rdf:resource="#NSPM-20"/>
  <includes rdf:resource="#radiologicalContingencyPlanning"/>
  <relatesTo rdf:resource="#ensuringSafetyAndMissionSuccess"/>
  <establishes rdf:resource="#aFramework"/>
</rdf:Description>

<rdf:Description rdf:about="#managingAndOverseeingNASAsNuclearFlightSafetyActivities">
  <rdf:type rdf:resource="#RoleAndResponsibility"/>
</rdf:Description>

<rdf:Description rdf:about="#theRequirements">
  <rdf:type rdf:resource="#Requirement"/>
  <allows rdf:resource="#DOENuclearSafetyAndSecurityRequirements"/>
  <allows rdf:resource="#USAirAndSpaceForceRangeSafetyRequirements"/>
  <allows rdf:resource="#NASAPayloadSafetyProcesses"/>
</rdf:Description>

<rdf:Description rdf:about="#NASAsPolicy">
  <rdf:type rdf:resource="#Policy"/>
  <isToProtect rdf:resource="#thePublic"/>
  <isToProtect rdf:resource="#NASAWorkforce"/>
  <isToProtect rdf:resource="#highValueEquipmentAndProperty"/>
  <isToProtect rdf:resource="#theEnvironment"/>
</rdf:Description>

<rdf:Description rdf:about="#NASAActivitiesAndOperations">
  <rdf:type rdf:resource="#NASAActivity"/>
  <factor rdf:resource="#safety"/>
</rdf:Description>

<rdf:Description rdf:about="#safety">
  <rdf:type rdf:resource="#Safety"/>
  <isAnIntegralFeatureOf rdf:resource="#programs"/>
  <isAnIntegralFeatureOf rdf:resource="#projects"/>
  <isAnIntegralFeatureOf rdf:resource="#technologies"/>
  <isAnIntegralFeatureOf rdf:resource="#operations"/>
  <isAnIntegralFeatureOf rdf:resource="#facilities"/>
</rdf:Description>

<rdf:Description rdf:about="#NSPM-20">
  <rdf:type rdf:resource="#Document"/>
  <is>Presidential Memorandum on Launch of Spacecraft Containing Space Nuclear Systems</is>
  <is>dated August 20, 2019</is>
</rdf:Description>

<rdf:Description rdf:about="#radiologicalContingencyPlanning">
  <rdf:type rdf:resource="#Activity"/>
</rdf:Description>

<rdf:Description rdf:about="#ensuringSafetyAndMissionSuccess">
  <rdf:type rdf:resource="#SafetyAndMissionAssuranceProcess"/>
  <isFor rdf:resource="#NASASponsoredPayloads"/>
</rdf:Description>

<rdf:Description rdf:about="#NASASponsoredPayloads">
  <rdf:type rdf:resource="#Material"/>
  <contains rdf:resource="#spaceNuclearSystemsOrOtherRadioactiveMaterial"/>
</rdf:Description>

<rdf:Description rdf:about="#aFramework">
  <rdf:type rdf:resource="#Framework"/>
  <isPartOf rdf:resource="#theOverallSafetyAndMissionAssuranceProcess"/>
</rdf:Description>

<rdf:Description rdf:about="#DOENuclearSafetyAndSecurityRequirements">
  <rdf:type rdf:resource="#Requirement"/>
</rdf:Description>

<rdf:Description rdf:about="#USAirAndSpaceForceRangeSafetyRequirements">
  <rdf:type rdf:resource="#Requirement"/>
</rdf:Description>

<rdf:Description rdf:about="#NASAPayloadSafetyProcesses">
  <rdf:type rdf:resource="#Requirement"/>
</rdf:Description>

<rdf:Description rdf:about="#theOverallSafetyAndMissionAssuranceProcess">
  <rdf:type rdf:resource="#SafetyAndMissionAssuranceProcess"/>
</rdf:Description>

<rdf:Description rdf:about="#thePublic">
  <rdf:type rdf:resource="#Material"/>
</rdf:Description>

<rdf:Description rdf:about="#NASAWorkforce">
  <rdf:type rdf:resource="#Material"/>
</rdf:Description>

<rdf:Description rdf:about="#highValueEquipmentAndProperty">
  <rdf:type rdf:resource="#Material"/>
</rdf:Description>

<rdf:Description rdf:about="#theEnvironment">
  <rdf:type rdf:resource="#Material"/>
</rdf:Description>

<rdf:Description rdf:about="#spaceNuclearSystemsOrOtherRadioactiveMaterial">
  <rdf:type rdf:resource="#Material"/>
</rdf:Description>

<rdf:Description rdf:about="#programs">
  <rdf:type rdf:resource="#Activity"/>
</rdf:Description>

<rdf:Description rdf:about="#projects">
  <rdf:type rdf:resource="#Activity"/>
</rdf:Description>

<rdf:Description rdf:about="#technologies">
  <rdf:type rdf:resource="#Activity"/>
</rdf:Description>

<rdf:Description rdf:about="#operations">
  <rdf:type rdf:resource="#Activity"/>
</rdf:Description>

<rdf:Description rdf:about="#facilities">
  <rdf:type rdf:resource="#Activity"/>
</rdf:Description>

</rdf:RDF>
'''

response = requests.put(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
