---
layout: post
title: "New in Low Baseline Support: Text tracks"
tags: baseline-low media-elements html-elements
---

[caniuse](https://caniuse.com/?search=text-tracks) · [spec](https://html.spec.whatwg.org/multipage/media.html#timed-text-tracks)

The `<track>` element is used as a child of the media elements that lets you specify a timed text track to be displayed in parallel with the media element.

### Source features

- ``api.HTMLMediaElement.addTextTrack`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLMediaElement.addTextTrack)
- ``api.HTMLTrackElement`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement)
- ``api.HTMLTrackElement.default`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.default)
- ``api.HTMLTrackElement.kind`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.kind)
- ``api.HTMLTrackElement.label`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.label)
- ``api.HTMLTrackElement.readyState`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.readyState)
- ``api.HTMLTrackElement.src`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.src)
- ``api.HTMLTrackElement.srclang`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.srclang)
- ``api.HTMLTrackElement.track`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.track)
- ``api.TextTrackCueList`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCueList)
- ``api.TextTrackCueList.getCueById`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCueList.getCueById)
- ``api.TextTrackCueList.length`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCueList.length)
- ``html.elements.track`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=html.elements.track)
- ``html.elements.track.default`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=html.elements.track.default)
- ``html.elements.track.kind`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=html.elements.track.kind)
- ``html.elements.track.label`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=html.elements.track.label)
- ``html.elements.track.srclang`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=html.elements.track.srclang)
- ``api.TextTrack`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack)
- ``api.TextTrack.activeCues`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.activeCues)
- ``api.TextTrack.addCue`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.addCue)
- ``api.TextTrack.cuechange_event`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.cuechange_event)
- ``api.TextTrack.cues`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.cues)
- ``api.TextTrack.kind`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.kind)
- ``api.TextTrack.label`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.label)
- ``api.TextTrack.language`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.language)
- ``api.TextTrack.mode`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.mode)
- ``api.TextTrack.removeCue`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.removeCue)
- ``api.TextTrackCue`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue)
- ``api.TextTrackCue.endTime`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue.endTime)
- ``api.TextTrackCue.enter_event`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue.enter_event)
- ``api.TextTrackCue.exit_event`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue.exit_event)
- ``api.TextTrackCue.id`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue.id)
- ``api.TextTrackCue.pauseOnExit`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue.pauseOnExit)
- ``api.TextTrackCue.startTime`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue.startTime)
- ``api.TextTrackCue.track`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackCue.track)
- ``api.TextTrackList`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackList)
- ``api.TextTrackList.addtrack_event`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackList.addtrack_event)
- ``api.TextTrackList.length`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackList.length)
- ``html.elements.track.src`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=html.elements.track.src)
- ``api.TextTrackList.change_event`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackList.change_event)
- ``api.TextTrackList.removetrack_event`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackList.removetrack_event)
- ``api.TextTrack.id`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.id)
- ``api.TextTrackList.getTrackById`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrackList.getTrackById)
- ``api.HTMLTrackElement.cuechange_event`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.HTMLTrackElement.cuechange_event)
- ``api.TextTrack.inBandMetadataTrackDispatchType`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.TextTrack.inBandMetadataTrackDispatchType)
