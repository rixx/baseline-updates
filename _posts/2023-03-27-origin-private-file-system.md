---
layout: post
title: "New in Low Baseline Support: Origin private file system"
tags: baseline-low file-system
---

[caniuse](https://caniuse.com/?search=origin-private-file-system) · [mdn](https://developer.mozilla.org/en-US/search?q=Origin private file system) · [spec](https://fs.spec.whatwg.org/#origin-private-file-system)

The `navigator.storage.getDirectory()` method returns a `FileSystemDirectoryHandle` that is restricted to a specific origin and invisible to the user's actual file system for faster file-based applications, such as SQLite databases.

### Source features

- ``api.FileSystemDirectoryHandle`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle)
- ``api.FileSystemDirectoryHandle.entries`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.entries)
- ``api.FileSystemDirectoryHandle.getDirectoryHandle`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.getDirectoryHandle)
- ``api.FileSystemDirectoryHandle.getFileHandle`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.getFileHandle)
- ``api.FileSystemDirectoryHandle.keys`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.keys)
- ``api.FileSystemDirectoryHandle.removeEntry`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.removeEntry)
- ``api.FileSystemDirectoryHandle.resolve`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.resolve)
- ``api.FileSystemDirectoryHandle.values`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.values)
- ``api.FileSystemFileHandle`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemFileHandle)
- ``api.FileSystemFileHandle.getFile`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemFileHandle.getFile)
- ``api.FileSystemHandle`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle)
- ``api.FileSystemHandle.isSameEntry`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle.isSameEntry)
- ``api.FileSystemHandle.kind`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle.kind)
- ``api.FileSystemHandle.name`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle.name)
- ``api.StorageManager.getDirectory`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.StorageManager.getDirectory)
- ``api.FileSystemFileHandle.createSyncAccessHandle`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemFileHandle.createSyncAccessHandle)
- ``api.FileSystemSyncAccessHandle`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle)
- ``api.FileSystemSyncAccessHandle.close`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.close)
- ``api.FileSystemSyncAccessHandle.flush`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.flush)
- ``api.FileSystemSyncAccessHandle.getSize`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.getSize)
- ``api.FileSystemSyncAccessHandle.read`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.read)
- ``api.FileSystemSyncAccessHandle.truncate`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.truncate)
- ``api.FileSystemSyncAccessHandle.write`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.write)
- ``api.FileSystemSyncAccessHandle.close.sync_version`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.close.sync_version)
- ``api.FileSystemSyncAccessHandle.flush.sync_version`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.flush.sync_version)
- ``api.FileSystemSyncAccessHandle.getSize.sync_version`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.getSize.sync_version)
- ``api.FileSystemSyncAccessHandle.truncate.sync_version`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.truncate.sync_version)
