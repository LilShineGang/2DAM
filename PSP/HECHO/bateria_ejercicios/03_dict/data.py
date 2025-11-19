students = {
    1: {
        "name": "Alice",
        "age": 17,
        "grades": [5, 7, 7, 6]
    },
    2: {
        "name": "Bob",
        "age": 18,
        "grades": [7, 5, 4, 6]
    },
    3: {
        "name": "Mary",
        "age": 16,
        "grades": [9, 10, 9, 7]
    },
    4: {
        "name": "John",
        "age": 17,
        "grades": [5, 3, 2, 4]
    }
}

images = [
    {
        "Id": "sha256:9234e8fb04c47cfe0f49931e4ac7eb76fa904e33b7f8576aec0501c085f02516",
        "RepoTags": [
            "alpine:latest"
        ],
        "RepoDigests": [
            "alpine@sha256:4bcff63911fcb4448bd4fdacec207030997caf25e9bea4045fa6c8c44de311d1"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-07-15T11:01:16Z",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 8306489,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/7eace3ddd7749db779187074272a243086eee5c37108e568bb5aeb714f656f74/merged",
                "UpperDir": "/var/lib/docker/overlay2/7eace3ddd7749db779187074272a243086eee5c37108e568bb5aeb714f656f74/diff",
                "WorkDir": "/var/lib/docker/overlay2/7eace3ddd7749db779187074272a243086eee5c37108e568bb5aeb714f656f74/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:418dccb7d85a63a6aa574439840f7a6fa6fd2321b3e2394568a317735e867d35"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        },
        "Config": {
            "Cmd": [
                "/bin/sh"
            ],
            "Entrypoint": None,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Labels": None,
            "OnBuild": None,
            "User": "",
            "Volumes": None,
            "WorkingDir": "/"
        }
    },
    {
        "Id": "sha256:77f2b24be2b3987f6d59918787d226acb4e6612644bacb3dd37adc494e477d9e",
        "RepoTags": [
            "python:latest"
        ],
        "RepoDigests": [
            "python@sha256:2deb0891ec3f643b1d342f04cc22154e6b6a76b41044791b537093fae00b6884"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-08-14T21:49:23Z",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 1108517276,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/f773c57bfd69a41013711503307e5f5516a56b567e926b0561a94138b674821a/diff:/var/lib/docker/overlay2/8ecc43bef7f65d8372038316e9ccbb637d310b982c9952859d7a0032592381e4/diff:/var/lib/docker/overlay2/2bbb116f6ccea1e12922e14e077f413e3e2c621236aa1cf32864c2730a3d0980/diff:/var/lib/docker/overlay2/22477171933abf2713c7d8bce3f6e4f1508edf116452b3a93abba5edb873ecf2/diff:/var/lib/docker/overlay2/5040891ac5075ca89cab3a74ce3fc3a5d170cca8715f43110868d0ff9c63ed58/diff:/var/lib/docker/overlay2/895f61c3365fe3ca237ab82dbc0d23dc96802f2d32c2976e5278dcf6079e18b1/diff",
                "MergedDir": "/var/lib/docker/overlay2/e6421a59837ecc1ccfd9c00d047304d62bb8f2bdf822bb5a808c2612dc09812d/merged",
                "UpperDir": "/var/lib/docker/overlay2/e6421a59837ecc1ccfd9c00d047304d62bb8f2bdf822bb5a808c2612dc09812d/diff",
                "WorkDir": "/var/lib/docker/overlay2/e6421a59837ecc1ccfd9c00d047304d62bb8f2bdf822bb5a808c2612dc09812d/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:185e04da9d947141fd703dbf36361bdc2ff77cc27cbf500fb9f4881cb5ddbe95",
                "sha256:607ddfe5f3c3f9e9df2b45f6275ad18bc76e49fdebcf0777c1c02c66f5012956",
                "sha256:0dd5860cbc60e77cc364ce36be1a9055d4139f2123324e14f756af1af719ffb0",
                "sha256:08e14ec5b7497da231d70d47d1d80440ba7d9997d43c0796a8394923bbc98183",
                "sha256:a9410d27207aec98b812b3d965ca2e03275f827993d34d4c0d13626efbe30415",
                "sha256:d52ca6ce2fa3c9595355a8a2519d36919e3414dc002d47aa8fcadeac1fdb8b74",
                "sha256:bafcf71d651a5230ebe9650cbcb4f874a7536f246844a2509f1118f6cde243bc"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        },
        "Config": {
            "Cmd": [
                "python3"
            ],
            "Entrypoint": None,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305",
                "PYTHON_VERSION=3.13.7",
                "PYTHON_SHA256=5462f9099dfd30e238def83c71d91897d8caa5ff6ebc7a50f14d4802cdaaa79a"
            ],
            "Labels": None,
            "OnBuild": None,
            "User": "",
            "Volumes": None,
            "WorkingDir": ""
        }
    }
]
