import { useEffect, useState } from "react";
import { SearchOutlined } from "@ant-design/icons";
import { Flex, Layout, Input, Table } from "antd";

import json_features from "../assets/features.json";

interface Feature {
	key: number;
	feature: string;
	place_id: string;
	review_id: string;
}

const columns = [
	{
		title: "Feature",
		dataIndex: "feature",
		key: "feature",
	},
	{
		title: "place_id",
		dataIndex: "place_id",
		key: "place_id",
	},
];

const App = () => {
	const [features, setFeatures] = useState<Feature[]>([]);
	const [search, setSearch] = useState("");

	useEffect(() => {
		setFeatures(json_features);
	}, []);

	// Filter features based on search input
	useEffect(() => {
		const filteredFeatures = json_features.filter((feature: Feature) =>
			feature.feature.toLowerCase().includes(search.toLowerCase())
		) as Feature[];
		setFeatures(filteredFeatures);
	}, [search]);

	return (
		<Flex
			justify='space-between'
			align='center'
			gap='middle'
			vertical
			style={{
				padding: "1rem",
			}}
		>
			<Input
				size='large'
				placeholder='large size'
				prefix={<SearchOutlined />}
				onChange={(e) => setSearch(e.target.value)}
			/>
			<Layout style={{ width: "100%" }}>
				<Table
					dataSource={features}
					columns={columns}
					pagination={{ pageSize: 50 }}
				/>
			</Layout>
		</Flex>
	);
};

export default App;
