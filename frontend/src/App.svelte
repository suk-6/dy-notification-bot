<script lang="ts">
	let content: string = "";

	const sendMessage = (send: string) => {
		if (content === "") {
			alert("메세지를 입력해주세요.");
			return;
		}

		const password = prompt("비밀번호를 입력해주세요.");
		if (password === null) return;
		console.log(
			JSON.stringify({
				content,
				password,
				send,
			})
		);

		fetch("/notification", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				content,
				password,
				send,
			}),
		})
			.then((res) => res.json())
			.then((data) => {
				if (data.success) {
					alert("메세지를 성공적으로 전송했습니다.");
				} else {
					alert("비밀번호가 틀렸습니다.");
				}
			});
	};
</script>

<main>
	<div class="grid gap-6">
		<div class="space-y-1">
			<h1
				class="peer-disabled:cursor-not-allowed peer-disabled:opacity-70 font-medium"
			>
				DY@Software 전체 메세지 전송
			</h1>
		</div>
		<div class="space-y-1">
			<label
				class="peer-disabled:cursor-not-allowed peer-disabled:opacity-70 text-sm font-medium"
				for="content"
			>
				메세지
			</label>
			<textarea
				class="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 min-h-[150px]"
				id="content"
				placeholder="메세지를 작성해주세요."
				bind:value={content}
				required
			></textarea>
		</div>
		<div class="grid grid-cols-2 gap-4">
			<button
				class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2"
				on:click={() => sendMessage("student")}
			>
				학생에게 전송하기
			</button>
			<button
				class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2"
				type="submit"
			>
				선생님에게 전송하기
			</button>
		</div>
	</div>
</main>
