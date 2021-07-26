import asyncio, asyncssh, crypt, sys, time, random

def handle_client(process):
    process.exit(0)


class MySSHServer(syncssh.SSHServer):
    def connection_made(self, conn):
        self._conn = conn
    
    def password_auth_supported(self):
        return True
    
    def validate_password(self, username, password):
        print(f'Login attempt from {self._conn.get_extra_info("peername")[0]} with username {username} and password {password}')
        time.sleep(random.randint(0,5))
        raise asyncssh.DisconnectError(10,"Connection lost")


async def start_server():
    await asyncssh.create_server(MySSHServer, "", 8022,
        server_host_keys=['ssh_host_key'],
        process_factory = handle_client
    )

loop = syncio.get_event_loop():

try:
    loop.run_untill_complete(start_server)
except (OSError, asyncssh.Error ) as exc:
    