<!--
SPDX-FileCopyrightText: Copyright (c) 2022-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

## REST to DataFrame Loader

[DataLoader](../../modules/core/data_loader.md) module is used to load data files content into a dataframe using custom loader function. This loader function can be configured to use different processing methods, such as single-threaded, multiprocess, dask, or dask_thread, as determined by the `MORPHEUS_FILE_DOWNLOAD_TYPE` environment variable. When download_method starts with "dask," a dask client is created to process the files, otherwise, a single thread or multiprocess is used.

After processing, the resulting dataframe is cached using a hash of the file paths. This loader also has the ability to load file content from S3 buckets, in addition to loading data from the disk.

### Example Loader Configuration

Using below configuration while loading DataLoader module, specifies that the DataLoader module should utilize the `rest` loader when loading files into a dataframe.

```json
{
	"loaders": [{
		"id": "rest"
	}]
}
```

**Note** :  Loaders can receive configuration from the `load` task via [control message](../../../source/control_message_guide.md) during runtime.

### Task Configurable Parameters

The parameters that can be configured for this specific loader at load task level:

| Parameter   | Type   | Description                         | Example Value | Default Value |
| ----------- | ------ | ----------------------------------- | ------------- | ------------- |
| `loader_id` | string | Unique identifier for the loader    | "rest"        | `[Required]`  |
| `strategy`  | string | Strategy for constructing dataframe | "aggregate"   | `[Required]`  |
| `queries`   | array  | parameters of REST queries          | See below     | `[Required]`  |


### `queries`

| Key            | Type       | Description                                                       | Example Value                                                                  | Default Value |
| -------------- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------- |
| `method`       | string     | Method of request                                                 | "GET"                                                                          | `"GET"`       |
| `endpoint`     | string     | Endpoint of request                                               | "0.0.0.0/path/to/target?param1=true"                                           | `[Required]`  |
| `content_type` | string     | Content type of request body in a POST request                    | "text/plain"                                                                   | `-`           |
| `body`         | string     | Request body in a POST request                                    | "param1=true&param2=false"                                                     | `-`           |
| `X-Headers`    | dictionary | Customized X-Headers of request                                   | "{"X-Header1":"header1", "X-Header2":"header2"}"                               | `-`           |
| `params`       | array      | Parameters of requested URL, override values included in endpoint | "[{"param1": "true", "param2":"false"}, {"param1": "false", "param2":"true"}]" | `-`           |


### Example Load Task Configuration

Below JSON configuration specifies how to pass additional configuration to the loader through a control message task at runtime.

```json
{
    "type":"load",
    "properties":
    {
        "loader_id":"rest",
        "strategy":"aggregate",
        "queries":[
            {
                "method":"<GET/POST>",
                "endpoint":"0.0.0.0/?param1=false&param2=true",
                "content_type":"text/plain",
                "body":"http POST body",
                "x-headers":
                {
                    "X-Header1":"header1",
                    "X-Header2":"header2"
                },
                "params":
                [
                    {
                        "param1":"true"
                    },
                    {
                        "param1":"false",
                        "param2":"true"
                    }
                ]
            }
        ]
    }
}
```