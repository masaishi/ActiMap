import { defineConfig } from "umi";

export default defineConfig({
	base: "/ActiMap/",
	publicPath: "/ActiMap/",
	routes: [
		{ path: "/", component: "index" },
		{ path: "/docs", component: "docs" },
	],
	npmClient: "pnpm",
});
