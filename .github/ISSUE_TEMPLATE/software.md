---
name: Software
about: Update list of vulnerable software
title: ''
labels: software-list
assignees: ''

---

**Please file a PR instead of an issue** if you can. See https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-another-users-repository. Thanks for your contribution!
- name: Setup .NET Core SDK
  uses: actions/setup-dotnet@v1.9.0
  with:
    # Optional SDK version(s) to use. If not provided, will install global.json version when available. Examples: 2.2.104, 3.1, 3.1.x
    dotnet-version: # optional
    # Optional package source for which to set up authentication. Will consult any existing NuGet.config in the root of the repo and provide a temporary NuGet.config using the NUGET_AUTH_TOKEN environment variable as a ClearTextPassword
    source-url: # optional
    # Optional OWNER for using packages from GitHub Package Registry organizations/users other than the current repository's owner. Only used if a GPR URL is also provided in source-url
    owner: # optional
    # Optional NuGet.config location, if your NuGet.config isn't located in the root of the repo.
    config-file: # optional
    # Whether prerelease versions should be matched with non-exact versions (for example 5.0.0-preview.6 being matched by 5, 5.0, 5.x or 5.0.x). Defaults to false if not provided.
    include-prerelease: # optional
