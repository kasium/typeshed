from typing import Any

class Runner:
    read_chunk_size: int
    input_sleep: float
    context: Any
    program_finished: Any
    warned_about_pty_fallback: bool
    watchers: Any
    def __init__(self, context) -> None: ...
    def run(self, command, **kwargs): ...
    def echo(self, command) -> None: ...
    def make_promise(self): ...
    def create_io_threads(self): ...
    def generate_result(self, **kwargs): ...
    def read_proc_output(self, reader) -> None: ...
    def write_our_output(self, stream, string) -> None: ...
    def handle_stdout(self, buffer_, hide, output) -> None: ...
    def handle_stderr(self, buffer_, hide, output) -> None: ...
    def read_our_stdin(self, input_): ...
    def handle_stdin(self, input_, output, echo) -> None: ...
    def should_echo_stdin(self, input_, output): ...
    def respond(self, buffer_) -> None: ...
    def generate_env(self, env, replace_env): ...
    def should_use_pty(self, pty, fallback): ...
    @property
    def has_dead_threads(self): ...
    def wait(self) -> None: ...
    def write_proc_stdin(self, data) -> None: ...
    def decode(self, data): ...
    @property
    def process_is_finished(self) -> None: ...
    def start(self, command, shell, env) -> None: ...
    def start_timer(self, timeout) -> None: ...
    def read_proc_stdout(self, num_bytes) -> None: ...
    def read_proc_stderr(self, num_bytes) -> None: ...
    def close_proc_stdin(self) -> None: ...
    def default_encoding(self): ...
    def send_interrupt(self, interrupt) -> None: ...
    def returncode(self) -> None: ...
    def stop(self) -> None: ...
    def stop_timer(self) -> None: ...
    def kill(self) -> None: ...
    @property
    def timed_out(self): ...

class Local(Runner):
    status: Any
    def __init__(self, context) -> None: ...
    def should_use_pty(self, pty: bool = ..., fallback: bool = ...): ...
    process: Any

class Result:
    stdout: str
    stderr: str
    encoding: str
    command: str
    shell: Any
    env: Any
    exited: int
    pty: bool
    hide: Union[
        tuple[()],
        tuple[Literal['stdout']],
        tuple[Literal['stderr']],
        tuple[Literal['stderr'], Literal['stdout']],
        tuple[Literal['stdout'], Literal['stderr']],
    ]
    def __init__(
        self,
        stdout: str = ...,
        stderr: str = ...,
        encoding=...,
        command: str = ...,
        shell: str = ...,
        env=...,
        exited: int = ...,
        pty: bool = ...,
        hide=...,
    ) -> None: ...
    @property
    def return_code(self): ...
    def __nonzero__(self) -> bool:
    def __bool__(self) -> bool:
    @property
    def ok(self) -> bool:
    @property
    def failed(self) -> bool:
    def tail(self, stream: Literal['stderr', 'stdout'], count: int = ...) -> str:

class Promise(Result):
    runner: Any
    def __init__(self, runner) -> None: ...
    def join(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

def normalize_hide(val, out_stream=..., err_stream=...): ...
def default_encoding() -> str: ...
