<script>
 	import '../app.css';
	import {browser} from '$app/environment'

 import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  onMount(() => {
	if (browser) {
		const token = localStorage.getItem('token');
    if (token) {
      document.cookie = `auth_token=${token}; max-age=${30 * 24 * 60 * 60}; path=/; SameSite=Strict`;
    }
  }});

  function handleLogout() {
	if (browser) {
		localStorage.removeItem('token');
		document.cookie = 'auth_token=; max-age=0; path=/; SameSite=Strict';
		goto('/login');
  }}
</script>


<slot />
