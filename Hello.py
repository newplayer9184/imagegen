# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import openai
LOGGER = get_logger(__name__)

def generate_image(prompt):
  client=openai.OpenAI(api_key=st.secrets["openai_api_key"])
  response=client.images.generate(
    prompt=prompt,
    n=1,
    size="256x256"
  )
  image_url= response.data[0].url
  return image_url
def image_gen() -> None:
    st.set_page_config(
        page_title="Hello i make image",
        page_icon="👋",
    )
    st.markdown("# Think of something")
    st.button("Run")

    input_text = st.text_area("What image would you like to generate?")
    run_button=st.button("Run")

    if run_button and input_text.strip() != "":
      with st.spinner("Buffering"):
        image_url = generate_image(input_text)
        st.image(image_url)
    else:
        st.warning("No input.")
    st.image("https;//i.redd.it/vton9zwqv3f61.jpg")


    prompt= f"Help me generate an image based on the following: {image_style} {animal} {activity},with some additional information: {input_text}. Make sure it's interesting"
image_gen()
    

#need add col stuff
if __name__ == "__main__":
    run()
def run():
  st.set_page_config(
    page_title="OpenAI"
    page_icon=""
  )
  st.title("Generate an image!")
  col1,col2=st.columns([3,5])
