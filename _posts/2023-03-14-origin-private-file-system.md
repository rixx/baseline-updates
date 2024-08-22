---
layout: post
title: "New in Low Baseline Support: Origin private file system"
tags: baseline-low
---

[caniuse](https://caniuse.com/?search=origin-private-file-system) · [spec](https://fs.spec.whatwg.org/#origin-private-file-system)

The `navigator.storage.getDirectory()` method returns a `FileSystemDirectoryHandle` that is restricted to a specific origin and invisible to the user's actual file system for faster file-based applications, such as SQLite databases.

### Source features

- ``api.FileSystemDirectoryHandle [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle)``
- ``api.FileSystemDirectoryHandle.entries [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.entries)``
- ``api.FileSystemDirectoryHandle.getDirectoryHandle [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.getDirectoryHandle)``
- ``api.FileSystemDirectoryHandle.getFileHandle [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.getFileHandle)``
- ``api.FileSystemDirectoryHandle.keys [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.keys)``
- ``api.FileSystemDirectoryHandle.removeEntry [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.removeEntry)``
- ``api.FileSystemDirectoryHandle.resolve [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.resolve)``
- ``api.FileSystemDirectoryHandle.values [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemDirectoryHandle.values)``
- ``api.FileSystemFileHandle [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemFileHandle)``
- ``api.FileSystemFileHandle.getFile [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemFileHandle.getFile)``
- ``api.FileSystemHandle [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle)``
- ``api.FileSystemHandle.isSameEntry [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle.isSameEntry)``
- ``api.FileSystemHandle.kind [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle.kind)``
- ``api.FileSystemHandle.name [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemHandle.name)``
- ``api.StorageManager.getDirectory [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.StorageManager.getDirectory)``
- ``api.FileSystemFileHandle.createSyncAccessHandle [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemFileHandle.createSyncAccessHandle)``
- ``api.FileSystemSyncAccessHandle [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle)``
- ``api.FileSystemSyncAccessHandle.close [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.close)``
- ``api.FileSystemSyncAccessHandle.flush [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.flush)``
- ``api.FileSystemSyncAccessHandle.getSize [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.getSize)``
- ``api.FileSystemSyncAccessHandle.read [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.read)``
- ``api.FileSystemSyncAccessHandle.truncate [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.truncate)``
- ``api.FileSystemSyncAccessHandle.write [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.FileSystemSyncAccessHandle.write)``
