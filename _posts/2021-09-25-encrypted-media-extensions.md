---
layout: post
title: "New in High Baseline Support: Encrypted media extensions"
tags: baseline-high
---

[caniuse](https://caniuse.com/?search=encrypted-media-extensions) · [mdn](https://developer.mozilla.org/en-US/search?q=Encrypted media extensions) · [spec](https://w3c.github.io/encrypted-media/)

The `mediaKeys` property of `HTMLMediaElement` and the `navigator.requestMediaKeySystemAccess()` method control the playback of content subject to digital rights management. Also known as EME.

### Source features

- ``api.HTMLMediaElement.encrypted_event`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLMediaElement.encrypted_event)
- ``api.HTMLMediaElement.mediaKeys`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLMediaElement.mediaKeys)
- ``api.HTMLMediaElement.setMediaKeys`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLMediaElement.setMediaKeys)
- ``api.MediaEncryptedEvent`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaEncryptedEvent)
- ``api.MediaEncryptedEvent.MediaEncryptedEvent`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaEncryptedEvent.MediaEncryptedEvent)
- ``api.MediaEncryptedEvent.initData`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaEncryptedEvent.initData)
- ``api.MediaEncryptedEvent.initDataType`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaEncryptedEvent.initDataType)
- ``api.MediaKeyMessageEvent`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyMessageEvent)
- ``api.MediaKeyMessageEvent.MediaKeyMessageEvent`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyMessageEvent.MediaKeyMessageEvent)
- ``api.MediaKeyMessageEvent.message`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyMessageEvent.message)
- ``api.MediaKeyMessageEvent.messageType`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyMessageEvent.messageType)
- ``api.MediaKeySession`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession)
- ``api.MediaKeySession.close`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.close)
- ``api.MediaKeySession.closed`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.closed)
- ``api.MediaKeySession.expiration`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.expiration)
- ``api.MediaKeySession.generateRequest`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.generateRequest)
- ``api.MediaKeySession.keyStatuses`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.keyStatuses)
- ``api.MediaKeySession.load`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.load)
- ``api.MediaKeySession.remove`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.remove)
- ``api.MediaKeySession.sessionId`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.sessionId)
- ``api.MediaKeySession.update`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.update)
- ``api.MediaKeyStatusMap`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap)
- ``api.MediaKeyStatusMap.size`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.size)
- ``api.MediaKeySystemAccess`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySystemAccess)
- ``api.MediaKeySystemAccess.createMediaKeys`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySystemAccess.createMediaKeys)
- ``api.MediaKeySystemAccess.keySystem`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySystemAccess.keySystem)
- ``api.MediaKeys`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeys)
- ``api.MediaKeys.createSession`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeys.createSession)
- ``api.MediaKeys.setServerCertificate`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeys.setServerCertificate)
- ``api.Navigator.requestMediaKeySystemAccess`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.Navigator.requestMediaKeySystemAccess)
- ``api.MediaKeySystemAccess.getConfiguration`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySystemAccess.getConfiguration)
- ``api.MediaKeyStatusMap.get`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.get)
- ``api.MediaKeyStatusMap.has`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.has)
- ``api.MediaKeyStatusMap.forEach`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.forEach)
- ``api.MediaKeyStatusMap.entries`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.entries)
- ``api.MediaKeyStatusMap.keys`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.keys)
- ``api.MediaKeyStatusMap.values`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.values)
- ``api.MediaKeyStatusMap.@@iterator`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeyStatusMap.@@iterator)
- ``api.MediaKeySession.keystatuseschange_event`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.keystatuseschange_event)
- ``api.MediaKeySession.message_event`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeySession.message_event)
- ``api.HTMLMediaElement.waitingforkey_event`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLMediaElement.waitingforkey_event)
- ``html.elements.iframe.allow.encrypted-media`` [[mdn]](https://developer.mozilla.org/en-US/search?q=html.elements.iframe.allow.encrypted-media)
- ``api.MediaKeys.getStatusForPolicy`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaKeys.getStatusForPolicy)
- ``api.MediaCapabilities.decodingInfo.configuration_keySystemConfiguration_parameter`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.MediaCapabilities.decodingInfo.configuration_keySystemConfiguration_parameter)
- ``http.headers.Permissions-Policy.encrypted-media`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.headers.Permissions-Policy.encrypted-media)
