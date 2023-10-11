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

#include "morpheus/llm/fwd.hpp"
#include "morpheus/types.hpp"

#include <pybind11/pytypes.h>
#include <pymrc/types.hpp>

namespace morpheus::llm {

template <class BaseT = LLMNodeBase>
class PyLLMNodeBase : public BaseT
{
  public:
    using BaseT::BaseT;

    std::vector<std::string> get_input_names() const override;

    Task<std::shared_ptr<LLMContext>> execute(std::shared_ptr<LLMContext> context) override;

  private:
    std::map<std::shared_ptr<LLMNodeBase>, pybind11::object> m_py_nodes;
};

}  // namespace morpheus::llm
