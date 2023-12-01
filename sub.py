from langchain.llms import OpenAI
import os
from io import IOBase
from typing import Any, List, Optional, Union
import pandas as pd
from langchain.agents.agent import AgentExecutor
from langchain.schema.language_model import BaseLanguageModel
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent

from langchain.callbacks.manager import a  # debug get observation directly

# Keys for OpenAI's API

<<<<<<< HEAD
key = "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"
=======
key=""
>>>>>>> 534fb3825cd512f65e34c6e59f89cd632860933a
os.environ["OPENAI_API_KEY"] = key


def csv_to_df(
        llm: BaseLanguageModel,
        path: Union[str, IOBase, List[Union[str, IOBase]]],
        pandas_kwargs: Optional[dict] = None,
        **kwargs: Any,
) -> AgentExecutor:
    _kwargs = pandas_kwargs or {}
    global df
    if isinstance(path, (str, IOBase)):
        df = pd.read_csv(path, **_kwargs)
    elif isinstance(path, list):
        df = []
        for item in path:
            if not isinstance(item, (str, IOBase)):
                raise ValueError(f"Expected str or file-like object, got {type(path)}")
            df.append(pd.read_csv(item, **_kwargs))
    else:
        raise ValueError(f"Expected str, list, or file-like object, got {type(path)}")
    return create_pandas_dataframe_agent(llm, df, **kwargs)


def parse_cmd(p_cmd: str):
    code_string = """
# Assuming 'pd' is the pandas
# Assuming 'df' is the DataFrame
pd.set_option("display.max_rows",None)
global cmd_out
cmd_out={cmd}
""".format(cmd=p_cmd)
    return code_string


def run_q(query: str):
    agent = csv_to_df(OpenAI(temperature=0,model='gpt-3.5-turbo-instruct'),
                      'uni-formatted.csv',
                      verbose=True)

    fin_out = agent.run(query)
    from langchain.tools.base import p_cmd
    pd.set_option("display.max_rows", None)
    cmd = parse_cmd(p_cmd)
    exec(cmd)
    #print(cmd_out)
    return cmd_out,fin_out


#run_q("List of employees whose name starts with a")
