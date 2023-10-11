/*
 * SPDX-FileCopyrightText: Copyright (c) 2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
 * SPDX-License-Identifier: Apache-2.0
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include <string>
#include <vector>

namespace morpheus::llm {

struct InputMap
{
    std::string input_name;      // The name of the upstream node to use as input
    std::string node_name{"-"};  // The name of the input that the upstream node maps to. '-' is a placeholder for the
                                 // default input of the node
};

// Ordered mapping of input names (current node) to output names (from previous nodes)
using input_map_t = std::vector<InputMap>;

}  // namespace morpheus::llm
