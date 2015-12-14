'''
WARNING: this is auto generated. Change it at your risk.
'''
SPECS={u'DiagnosticReport': {'searchParams': {u'codedDiagnosis': 'token', u'code': 'token', u'text': 'string', u'image': 'string', u'meta': 'string', u'result': 'reference', u'conclusion': 'string', u'image-link': 'reference', u'id': 'string', u'subject': 'reference', u'category': 'token', u'modifierExtension': 'string', u'performer': 'reference', u'contained': 'string', u'issued': 'date', u'image-modifierExtension': 'string', u'image-comment': 'string', u'effective[x]': 'date', u'status': 'token', u'image-extension': 'string', u'specimen': 'reference', u'image-id': 'string', u'presentedForm': 'string', u'encounter': 'reference', u'implicitRules': 'string', u'language': 'token', u'extension': 'string', u'request': 'reference', u'imagingStudy': 'reference', u'identifier': 'token'}, 'elements': [{'path': u'DiagnosticReport', 'definition': {'max': u'*', 'type': [{u'code': u'DomainResource'}], 'min': 0}}, {'path': u'DiagnosticReport.id', 'searchParam': {'type': 'string', 'name': u'id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'DiagnosticReport.meta', 'searchParam': {'type': 'string', 'name': u'meta'}, 'definition': {'max': u'1', 'type': [{u'code': u'Meta'}], 'min': 0}}, {'path': u'DiagnosticReport.implicitRules', 'searchParam': {'type': 'string', 'name': u'implicitRules'}, 'definition': {'max': u'1', 'type': [{u'code': u'uri'}], 'min': 0}}, {'path': u'DiagnosticReport.language', 'searchParam': {'type': 'token', 'name': u'language'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 0}}, {'path': u'DiagnosticReport.text', 'searchParam': {'type': 'string', 'name': u'text'}, 'definition': {'max': u'1', 'type': [{u'code': u'Narrative'}], 'min': 0}}, {'path': u'DiagnosticReport.contained', 'searchParam': {'type': 'string', 'name': u'contained'}, 'definition': {'max': u'*', 'type': [{u'code': u'Resource'}], 'min': 0}}, {'path': u'DiagnosticReport.extension', 'searchParam': {'type': 'string', 'name': u'extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'DiagnosticReport.modifierExtension', 'searchParam': {'type': 'string', 'name': u'modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'DiagnosticReport.identifier', 'searchParam': {'type': 'token', 'name': u'identifier'}, 'definition': {'max': u'*', 'type': [{u'code': u'Identifier'}], 'min': 0}}, {'path': u'DiagnosticReport.status', 'searchParam': {'type': 'token', 'name': u'status'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 1}}, {'path': u'DiagnosticReport.category', 'searchParam': {'type': 'token', 'name': u'category'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'DiagnosticReport.code', 'searchParam': {'type': 'token', 'name': u'code'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 1}}, {'path': u'DiagnosticReport.subject', 'searchParam': {'type': 'reference', 'name': u'subject'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Patient'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Group'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Device'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Location'], u'code': u'Reference'}], 'min': 1}}, {'path': u'DiagnosticReport.encounter', 'searchParam': {'type': 'reference', 'name': u'encounter'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Encounter'], u'code': u'Reference'}], 'min': 0}}, {'path': u'DiagnosticReport.effective[x]', 'searchParam': {'type': 'date', 'name': u'effective[x]'}, 'definition': {'max': u'1', 'type': [{u'code': u'dateTime'}, {u'code': u'Period'}], 'min': 1}}, {'path': u'DiagnosticReport.issued', 'searchParam': {'type': 'date', 'name': u'issued'}, 'definition': {'max': u'1', 'type': [{u'code': u'instant'}], 'min': 1}}, {'path': u'DiagnosticReport.performer', 'searchParam': {'type': 'reference', 'name': u'performer'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Practitioner'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Organization'], u'code': u'Reference'}], 'min': 1}}, {'path': u'DiagnosticReport.request', 'searchParam': {'type': 'reference', 'name': u'request'}, 'definition': {'max': u'*', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/DiagnosticOrder'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/ProcedureRequest'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/ReferralRequest'], u'code': u'Reference'}], 'min': 0}}, {'path': u'DiagnosticReport.specimen', 'searchParam': {'type': 'reference', 'name': u'specimen'}, 'definition': {'max': u'*', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Specimen'], u'code': u'Reference'}], 'min': 0}}, {'path': u'DiagnosticReport.result', 'searchParam': {'type': 'reference', 'name': u'result'}, 'definition': {'max': u'*', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Observation'], u'code': u'Reference'}], 'min': 0}}, {'path': u'DiagnosticReport.imagingStudy', 'searchParam': {'type': 'reference', 'name': u'imagingStudy'}, 'definition': {'max': u'*', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/ImagingStudy'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/ImagingObjectSelection'], u'code': u'Reference'}], 'min': 0}}, {'path': u'DiagnosticReport.image', 'searchParam': {'type': 'string', 'name': u'image'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'DiagnosticReport.image.id', 'searchParam': {'type': 'string', 'name': u'image-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'DiagnosticReport.image.extension', 'searchParam': {'type': 'string', 'name': u'image-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'DiagnosticReport.image.modifierExtension', 'searchParam': {'type': 'string', 'name': u'image-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'DiagnosticReport.image.comment', 'searchParam': {'type': 'string', 'name': u'image-comment'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'DiagnosticReport.image.link', 'searchParam': {'type': 'reference', 'name': u'image-link'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Media'], u'code': u'Reference'}], 'min': 1}}, {'path': u'DiagnosticReport.conclusion', 'searchParam': {'type': 'string', 'name': u'conclusion'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'DiagnosticReport.codedDiagnosis', 'searchParam': {'type': 'token', 'name': u'codedDiagnosis'}, 'definition': {'max': u'*', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'DiagnosticReport.presentedForm', 'searchParam': {'type': 'string', 'name': u'presentedForm'}, 'definition': {'max': u'*', 'type': [{u'code': u'Attachment'}], 'min': 0}}]}, u'Patient': {'searchParams': {u'contact-id': 'string', u'animal-breed': 'token', u'link-modifierExtension': 'string', u'maritalStatus': 'token', u'contact-address': 'string', u'animal-modifierExtension': 'string', u'telecom': 'token', u'photo': 'string', u'link-other': 'reference', u'communication': 'string', u'birthDate': 'date', u'contact-gender': 'token', u'multipleBirth[x]': 'token', u'meta': 'string', u'link-id': 'string', u'id': 'string', u'communication-preferred': 'token', u'contact-extension': 'string', u'contact-telecom': 'token', u'contact-period': 'date', u'managingOrganization': 'reference', u'modifierExtension': 'string', u'communication-id': 'string', u'deceased[x]': 'token', u'contained': 'string', u'animal': 'string', u'text': 'string', u'implicitRules': 'string', u'contact-relationship': 'token', u'animal-extension': 'string', u'communication-extension': 'string', u'contact-modifierExtension': 'string', u'animal-id': 'string', u'link': 'string', u'address': 'string', u'active': 'token', u'careProvider': 'reference', u'link-extension': 'string', u'name': 'string', u'contact-name': 'string', u'language': 'token', u'extension': 'string', u'gender': 'token', u'animal-genderStatus': 'token', u'link-type': 'token', u'communication-language': 'token', u'contact': 'string', u'animal-species': 'token', u'contact-organization': 'reference', u'identifier': 'token', u'communication-modifierExtension': 'string'}, 'elements': [{'path': u'Patient', 'definition': {'max': u'*', 'type': [{u'code': u'DomainResource'}], 'min': 0}}, {'path': u'Patient.id', 'searchParam': {'type': 'string', 'name': u'id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Patient.meta', 'searchParam': {'type': 'string', 'name': u'meta'}, 'definition': {'max': u'1', 'type': [{u'code': u'Meta'}], 'min': 0}}, {'path': u'Patient.implicitRules', 'searchParam': {'type': 'string', 'name': u'implicitRules'}, 'definition': {'max': u'1', 'type': [{u'code': u'uri'}], 'min': 0}}, {'path': u'Patient.language', 'searchParam': {'type': 'token', 'name': u'language'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 0}}, {'path': u'Patient.text', 'searchParam': {'type': 'string', 'name': u'text'}, 'definition': {'max': u'1', 'type': [{u'code': u'Narrative'}], 'min': 0}}, {'path': u'Patient.contained', 'searchParam': {'type': 'string', 'name': u'contained'}, 'definition': {'max': u'*', 'type': [{u'code': u'Resource'}], 'min': 0}}, {'path': u'Patient.extension', 'searchParam': {'type': 'string', 'name': u'extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.modifierExtension', 'searchParam': {'type': 'string', 'name': u'modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.identifier', 'searchParam': {'type': 'token', 'name': u'identifier'}, 'definition': {'max': u'*', 'type': [{u'code': u'Identifier'}], 'min': 0}}, {'path': u'Patient.active', 'searchParam': {'type': 'token', 'name': u'active'}, 'definition': {'max': u'1', 'type': [{u'code': u'boolean'}], 'min': 0}}, {'path': u'Patient.name', 'searchParam': {'type': 'string', 'name': u'name'}, 'definition': {'max': u'*', 'type': [{u'code': u'HumanName'}], 'min': 0}}, {'path': u'Patient.telecom', 'searchParam': {'type': 'token', 'name': u'telecom'}, 'definition': {'max': u'*', 'type': [{u'code': u'ContactPoint'}], 'min': 0}}, {'path': u'Patient.gender', 'searchParam': {'type': 'token', 'name': u'gender'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 0}}, {'path': u'Patient.birthDate', 'searchParam': {'type': 'date', 'name': u'birthDate'}, 'definition': {'max': u'1', 'type': [{u'code': u'date'}], 'min': 0}}, {'path': u'Patient.deceased[x]', 'searchParam': {'type': 'token', 'name': u'deceased[x]'}, 'definition': {'max': u'1', 'type': [{u'code': u'boolean'}, {u'code': u'dateTime'}], 'min': 0}}, {'path': u'Patient.address', 'searchParam': {'type': 'string', 'name': u'address'}, 'definition': {'max': u'*', 'type': [{u'code': u'Address'}], 'min': 0}}, {'path': u'Patient.maritalStatus', 'searchParam': {'type': 'token', 'name': u'maritalStatus'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Patient.multipleBirth[x]', 'searchParam': {'type': 'token', 'name': u'multipleBirth[x]'}, 'definition': {'max': u'1', 'type': [{u'code': u'boolean'}, {u'code': u'integer'}], 'min': 0}}, {'path': u'Patient.photo', 'searchParam': {'type': 'string', 'name': u'photo'}, 'definition': {'max': u'*', 'type': [{u'code': u'Attachment'}], 'min': 0}}, {'path': u'Patient.contact', 'searchParam': {'type': 'string', 'name': u'contact'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Patient.contact.id', 'searchParam': {'type': 'string', 'name': u'contact-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Patient.contact.extension', 'searchParam': {'type': 'string', 'name': u'contact-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.contact.modifierExtension', 'searchParam': {'type': 'string', 'name': u'contact-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.contact.relationship', 'searchParam': {'type': 'token', 'name': u'contact-relationship'}, 'definition': {'max': u'*', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Patient.contact.name', 'searchParam': {'type': 'string', 'name': u'contact-name'}, 'definition': {'max': u'1', 'type': [{u'code': u'HumanName'}], 'min': 0}}, {'path': u'Patient.contact.telecom', 'searchParam': {'type': 'token', 'name': u'contact-telecom'}, 'definition': {'max': u'*', 'type': [{u'code': u'ContactPoint'}], 'min': 0}}, {'path': u'Patient.contact.address', 'searchParam': {'type': 'string', 'name': u'contact-address'}, 'definition': {'max': u'1', 'type': [{u'code': u'Address'}], 'min': 0}}, {'path': u'Patient.contact.gender', 'searchParam': {'type': 'token', 'name': u'contact-gender'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 0}}, {'path': u'Patient.contact.organization', 'searchParam': {'type': 'reference', 'name': u'contact-organization'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Organization'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Patient.contact.period', 'searchParam': {'type': 'date', 'name': u'contact-period'}, 'definition': {'max': u'1', 'type': [{u'code': u'Period'}], 'min': 0}}, {'path': u'Patient.animal', 'searchParam': {'type': 'string', 'name': u'animal'}, 'definition': {'max': u'1', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Patient.animal.id', 'searchParam': {'type': 'string', 'name': u'animal-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Patient.animal.extension', 'searchParam': {'type': 'string', 'name': u'animal-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.animal.modifierExtension', 'searchParam': {'type': 'string', 'name': u'animal-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.animal.species', 'searchParam': {'type': 'token', 'name': u'animal-species'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 1}}, {'path': u'Patient.animal.breed', 'searchParam': {'type': 'token', 'name': u'animal-breed'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Patient.animal.genderStatus', 'searchParam': {'type': 'token', 'name': u'animal-genderStatus'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Patient.communication', 'searchParam': {'type': 'string', 'name': u'communication'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Patient.communication.id', 'searchParam': {'type': 'string', 'name': u'communication-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Patient.communication.extension', 'searchParam': {'type': 'string', 'name': u'communication-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.communication.modifierExtension', 'searchParam': {'type': 'string', 'name': u'communication-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.communication.language', 'searchParam': {'type': 'token', 'name': u'communication-language'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 1}}, {'path': u'Patient.communication.preferred', 'searchParam': {'type': 'token', 'name': u'communication-preferred'}, 'definition': {'max': u'1', 'type': [{u'code': u'boolean'}], 'min': 0}}, {'path': u'Patient.careProvider', 'searchParam': {'type': 'reference', 'name': u'careProvider'}, 'definition': {'max': u'*', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Organization'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Practitioner'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Patient.managingOrganization', 'searchParam': {'type': 'reference', 'name': u'managingOrganization'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Organization'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Patient.link', 'searchParam': {'type': 'string', 'name': u'link'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Patient.link.id', 'searchParam': {'type': 'string', 'name': u'link-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Patient.link.extension', 'searchParam': {'type': 'string', 'name': u'link-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.link.modifierExtension', 'searchParam': {'type': 'string', 'name': u'link-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Patient.link.other', 'searchParam': {'type': 'reference', 'name': u'link-other'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Patient'], u'code': u'Reference'}], 'min': 1}}, {'path': u'Patient.link.type', 'searchParam': {'type': 'token', 'name': u'link-type'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 1}}]}, u'Observation': {'searchParams': {u'code': 'token', u'valueReference': 'reference', u'referenceRange-age': 'string', u'text': 'string', u'component-value[x]': 'quantity', u'related': 'string', u'related-id': 'string', u'meta': 'string', u'bodySite': 'token', u'referenceRange-extension': 'string', u'referenceRange-low': 'quantity', u'component-id': 'string', u'interpretation': 'token', u'dataAbsentReason': 'token', u'id': 'string', u'subject': 'reference', u'category': 'token', u'modifierExtension': 'string', u'related-type': 'token', u'performer': 'reference', u'comments': 'string', u'contained': 'string', u'related-target': 'reference', u'issued': 'date', u'method': 'token', u'effective[x]': 'date', u'status': 'token', u'specimen': 'reference', u'component': 'string', u'device': 'reference', u'encounter': 'reference', u'implicitRules': 'string', u'related-extension': 'string', u'related-modifierExtension': 'string', u'language': 'token', u'extension': 'string', u'component-code': 'token', u'referenceRange-text': 'string', u'referenceRange-meaning': 'token', u'referenceRange-modifierExtension': 'string', u'referenceRange': 'string', u'referenceRange-id': 'string', u'component-dataAbsentReason': 'token', u'component-extension': 'string', u'identifier': 'token', u'referenceRange-high': 'quantity', u'component-modifierExtension': 'string'}, 'elements': [{'path': u'Observation', 'definition': {'max': u'*', 'type': [{u'code': u'DomainResource'}], 'min': 0}}, {'path': u'Observation.id', 'searchParam': {'type': 'string', 'name': u'id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Observation.meta', 'searchParam': {'type': 'string', 'name': u'meta'}, 'definition': {'max': u'1', 'type': [{u'code': u'Meta'}], 'min': 0}}, {'path': u'Observation.implicitRules', 'searchParam': {'type': 'string', 'name': u'implicitRules'}, 'definition': {'max': u'1', 'type': [{u'code': u'uri'}], 'min': 0}}, {'path': u'Observation.language', 'searchParam': {'type': 'token', 'name': u'language'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 0}}, {'path': u'Observation.text', 'searchParam': {'type': 'string', 'name': u'text'}, 'definition': {'max': u'1', 'type': [{u'code': u'Narrative'}], 'min': 0}}, {'path': u'Observation.contained', 'searchParam': {'type': 'string', 'name': u'contained'}, 'definition': {'max': u'*', 'type': [{u'code': u'Resource'}], 'min': 0}}, {'path': u'Observation.extension', 'searchParam': {'type': 'string', 'name': u'extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.modifierExtension', 'searchParam': {'type': 'string', 'name': u'modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.identifier', 'searchParam': {'type': 'token', 'name': u'identifier'}, 'definition': {'max': u'*', 'type': [{u'code': u'Identifier'}], 'min': 0}}, {'path': u'Observation.status', 'searchParam': {'type': 'token', 'name': u'status'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 1}}, {'path': u'Observation.category', 'searchParam': {'type': 'token', 'name': u'category'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Observation.code', 'searchParam': {'type': 'token', 'name': u'code'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 1}}, {'path': u'Observation.subject', 'searchParam': {'type': 'reference', 'name': u'subject'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Patient'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Group'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Device'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Location'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Observation.encounter', 'searchParam': {'type': 'reference', 'name': u'encounter'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Encounter'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Observation.effective[x]', 'searchParam': {'type': 'date', 'name': u'effective[x]'}, 'definition': {'max': u'1', 'type': [{u'code': u'dateTime'}, {u'code': u'Period'}], 'min': 0}}, {'path': u'Observation.issued', 'searchParam': {'type': 'date', 'name': u'issued'}, 'definition': {'max': u'1', 'type': [{u'code': u'instant'}], 'min': 0}}, {'path': u'Observation.performer', 'searchParam': {'type': 'reference', 'name': u'performer'}, 'definition': {'max': u'*', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Practitioner'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Organization'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/Patient'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/RelatedPerson'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Observation.valueReference', 'searchParam': {'type': 'reference', 'name': u'valueReference'}, 'definition': {'max': u'1', 'type': [{u'code': u'Reference'}], 'min': 0}}, {'path': u'Observation.dataAbsentReason', 'searchParam': {'type': 'token', 'name': u'dataAbsentReason'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Observation.interpretation', 'searchParam': {'type': 'token', 'name': u'interpretation'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Observation.comments', 'searchParam': {'type': 'string', 'name': u'comments'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'Observation.bodySite', 'searchParam': {'type': 'token', 'name': u'bodySite'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Observation.method', 'searchParam': {'type': 'token', 'name': u'method'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Observation.specimen', 'searchParam': {'type': 'reference', 'name': u'specimen'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Specimen'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Observation.device', 'searchParam': {'type': 'reference', 'name': u'device'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Device'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/DeviceMetric'], u'code': u'Reference'}], 'min': 0}}, {'path': u'Observation.referenceRange', 'searchParam': {'type': 'string', 'name': u'referenceRange'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Observation.referenceRange.id', 'searchParam': {'type': 'string', 'name': u'referenceRange-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Observation.referenceRange.extension', 'searchParam': {'type': 'string', 'name': u'referenceRange-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.referenceRange.modifierExtension', 'searchParam': {'type': 'string', 'name': u'referenceRange-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.referenceRange.low', 'searchParam': {'type': 'quantity', 'name': u'referenceRange-low'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/SimpleQuantity'], u'code': u'Quantity'}], 'min': 0}}, {'path': u'Observation.referenceRange.high', 'searchParam': {'type': 'quantity', 'name': u'referenceRange-high'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/SimpleQuantity'], u'code': u'Quantity'}], 'min': 0}}, {'path': u'Observation.referenceRange.meaning', 'searchParam': {'type': 'token', 'name': u'referenceRange-meaning'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Observation.referenceRange.age', 'searchParam': {'type': 'string', 'name': u'referenceRange-age'}, 'definition': {'max': u'1', 'type': [{u'code': u'Range'}], 'min': 0}}, {'path': u'Observation.referenceRange.text', 'searchParam': {'type': 'string', 'name': u'referenceRange-text'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'Observation.related', 'searchParam': {'type': 'string', 'name': u'related'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Observation.related.id', 'searchParam': {'type': 'string', 'name': u'related-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Observation.related.extension', 'searchParam': {'type': 'string', 'name': u'related-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.related.modifierExtension', 'searchParam': {'type': 'string', 'name': u'related-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.related.type', 'searchParam': {'type': 'token', 'name': u'related-type'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 0}}, {'path': u'Observation.related.target', 'searchParam': {'type': 'reference', 'name': u'related-target'}, 'definition': {'max': u'1', 'type': [{u'profile': [u'http://hl7.org/fhir/StructureDefinition/Observation'], u'code': u'Reference'}, {u'profile': [u'http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse'], u'code': u'Reference'}], 'min': 1}}, {'path': u'Observation.component', 'searchParam': {'type': 'string', 'name': u'component'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Observation.component.id', 'searchParam': {'type': 'string', 'name': u'component-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Observation.component.extension', 'searchParam': {'type': 'string', 'name': u'component-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.component.modifierExtension', 'searchParam': {'type': 'string', 'name': u'component-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Observation.component.code', 'searchParam': {'type': 'token', 'name': u'component-code'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 1}}, {'path': u'Observation.component.value[x]', 'searchParam': {'type': 'quantity', 'name': u'component-value[x]'}, 'definition': {'max': u'1', 'type': [{u'code': u'Quantity'}, {u'code': u'CodeableConcept'}, {u'code': u'string'}, {u'code': u'Range'}, {u'code': u'Ratio'}, {u'code': u'SampledData'}, {u'code': u'Attachment'}, {u'code': u'time'}, {u'code': u'dateTime'}, {u'code': u'Period'}], 'min': 0}}, {'path': u'Observation.component.dataAbsentReason', 'searchParam': {'type': 'token', 'name': u'component-dataAbsentReason'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Observation.component.referenceRange', 'searchParam': {'type': 'token', 'name': u'component-referenceRange'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}]}, u'Sequence': {'searchParams': {u'allelicFrequency': 'number', u'text': 'string', u'ga4gh-readGroupSetId': 'string', u'ga4gh-repository': 'string', u'allelicState': 'token', u'variation-variationHGVS': 'token', u'meta': 'string', u'coordinate-chromosome': 'token', u'id': 'string', u'readCoverage': 'number', u'referenceAllele': 'string', u'variation-variationType': 'token', u'coordinate-start': 'number', u'modifierExtension': 'string', u'coordinate-genomeBuild': 'token', u'ga4gh-id': 'string', u'coordinate-extension': 'string', u'species': 'token', u'source': 'token', u'contained': 'string', u'variation-extension': 'string', u'variation-referenceSeq': 'token', u'cigar': 'string', u'variation-quantity': 'quantity', u'variation': 'string', u'ga4gh': 'string', u'variation-modifierExtension': 'string', u'variation-type': 'token', u'copyNumberEvent': 'token', u'ga4gh-extension': 'string', u'variationID': 'token', u'coordinate-end': 'number', u'implicitRules': 'string', u'coordinate-id': 'string', u'ga4gh-modifierExtension': 'string', u'language': 'token', u'extension': 'string', u'observedAllele': 'string', u'region': 'token', u'variation-id': 'string', u'ga4gh-variantId': 'string', u'coordinate': 'string', u'gene': 'token', u'coordinate-modifierExtension': 'string'}, 'elements': [{'path': u'Sequence', 'definition': {'max': u'*', 'type': [{u'code': u'DomainResource'}], 'min': 0}}, {'path': u'Sequence.id', 'searchParam': {'type': 'string', 'name': u'id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Sequence.meta', 'searchParam': {'type': 'string', 'name': u'meta'}, 'definition': {'max': u'1', 'type': [{u'code': u'Meta'}], 'min': 0}}, {'path': u'Sequence.implicitRules', 'searchParam': {'type': 'string', 'name': u'implicitRules'}, 'definition': {'max': u'1', 'type': [{u'code': u'uri'}], 'min': 0}}, {'path': u'Sequence.language', 'searchParam': {'type': 'token', 'name': u'language'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 0}}, {'path': u'Sequence.text', 'searchParam': {'type': 'string', 'name': u'text'}, 'definition': {'max': u'1', 'type': [{u'code': u'Narrative'}], 'min': 0}}, {'path': u'Sequence.contained', 'searchParam': {'type': 'string', 'name': u'contained'}, 'definition': {'max': u'*', 'type': [{u'code': u'Resource'}], 'min': 0}}, {'path': u'Sequence.extension', 'searchParam': {'type': 'string', 'name': u'extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.modifierExtension', 'searchParam': {'type': 'string', 'name': u'modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.variationID', 'searchParam': {'type': 'token', 'name': u'variationID'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.variation', 'searchParam': {'type': 'string', 'name': u'variation'}, 'definition': {'max': u'*', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Sequence.variation.id', 'searchParam': {'type': 'string', 'name': u'variation-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Sequence.variation.extension', 'searchParam': {'type': 'string', 'name': u'variation-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.variation.modifierExtension', 'searchParam': {'type': 'string', 'name': u'variation-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.variation.type', 'searchParam': {'type': 'token', 'name': u'variation-type'}, 'definition': {'max': u'1', 'type': [{u'code': u'code'}], 'min': 1}}, {'path': u'Sequence.variation.variationHGVS', 'searchParam': {'type': 'token', 'name': u'variation-variationHGVS'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.variation.variationType', 'searchParam': {'type': 'token', 'name': u'variation-variationType'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.variation.referenceSeq', 'searchParam': {'type': 'token', 'name': u'variation-referenceSeq'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.variation.quantity', 'searchParam': {'type': 'quantity', 'name': u'variation-quantity'}, 'definition': {'max': u'1', 'type': [{u'code': u'Quantity'}], 'min': 0}}, {'path': u'Sequence.coordinate', 'searchParam': {'type': 'string', 'name': u'coordinate'}, 'definition': {'max': u'1', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Sequence.coordinate.id', 'searchParam': {'type': 'string', 'name': u'coordinate-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Sequence.coordinate.extension', 'searchParam': {'type': 'string', 'name': u'coordinate-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.coordinate.modifierExtension', 'searchParam': {'type': 'string', 'name': u'coordinate-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.coordinate.chromosome', 'searchParam': {'type': 'token', 'name': u'coordinate-chromosome'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.coordinate.start', 'searchParam': {'type': 'number', 'name': u'coordinate-start'}, 'definition': {'max': u'1', 'type': [{u'code': u'integer'}], 'min': 0}}, {'path': u'Sequence.coordinate.end', 'searchParam': {'type': 'number', 'name': u'coordinate-end'}, 'definition': {'max': u'1', 'type': [{u'code': u'integer'}], 'min': 0}}, {'path': u'Sequence.coordinate.genomeBuild', 'searchParam': {'type': 'token', 'name': u'coordinate-genomeBuild'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.gene', 'searchParam': {'type': 'token', 'name': u'gene'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.region', 'searchParam': {'type': 'token', 'name': u'region'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.species', 'searchParam': {'type': 'token', 'name': u'species'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.source', 'searchParam': {'type': 'token', 'name': u'source'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.observedAllele', 'searchParam': {'type': 'string', 'name': u'observedAllele'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'Sequence.referenceAllele', 'searchParam': {'type': 'string', 'name': u'referenceAllele'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'Sequence.cigar', 'searchParam': {'type': 'string', 'name': u'cigar'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'Sequence.allelicState', 'searchParam': {'type': 'token', 'name': u'allelicState'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.allelicFrequency', 'searchParam': {'type': 'number', 'name': u'allelicFrequency'}, 'definition': {'max': u'1', 'type': [{u'code': u'decimal'}], 'min': 0}}, {'path': u'Sequence.copyNumberEvent', 'searchParam': {'type': 'token', 'name': u'copyNumberEvent'}, 'definition': {'max': u'1', 'type': [{u'code': u'CodeableConcept'}], 'min': 0}}, {'path': u'Sequence.readCoverage', 'searchParam': {'type': 'number', 'name': u'readCoverage'}, 'definition': {'max': u'1', 'type': [{u'code': u'integer'}], 'min': 0}}, {'path': u'Sequence.ga4gh', 'searchParam': {'type': 'string', 'name': u'ga4gh'}, 'definition': {'max': u'1', 'type': [{u'code': u'BackboneElement'}], 'min': 0}}, {'path': u'Sequence.ga4gh.id', 'searchParam': {'type': 'string', 'name': u'ga4gh-id'}, 'definition': {'max': u'1', 'type': [{u'code': u'id'}], 'min': 0}}, {'path': u'Sequence.ga4gh.extension', 'searchParam': {'type': 'string', 'name': u'ga4gh-extension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.ga4gh.modifierExtension', 'searchParam': {'type': 'string', 'name': u'ga4gh-modifierExtension'}, 'definition': {'max': u'*', 'type': [{u'code': u'Extension'}], 'min': 0}}, {'path': u'Sequence.ga4gh.repository', 'searchParam': {'type': 'string', 'name': u'ga4gh-repository'}, 'definition': {'max': u'1', 'type': [{u'code': u'uri'}], 'min': 0}}, {'path': u'Sequence.ga4gh.variantId', 'searchParam': {'type': 'string', 'name': u'ga4gh-variantId'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}, {'path': u'Sequence.ga4gh.readGroupSetId', 'searchParam': {'type': 'string', 'name': u'ga4gh-readGroupSetId'}, 'definition': {'max': u'1', 'type': [{u'code': u'string'}], 'min': 0}}]}}
RESOURCES=set([u'DiagnosticReport', 'name', u'Observation', 'name', u'Patient', 'name', u'Sequence', 'name'])
REFERENCE_TYPES={u'DiagnosticReport': {}, u'Patient': {}, u'Observation': {}, u'Sequence': {}}