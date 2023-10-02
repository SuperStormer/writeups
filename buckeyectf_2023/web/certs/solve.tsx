import {
	Page,
	Text,
	View,
	Document,
	renderToBuffer,
	Image,
	Circle,
	Svg,
	Font,
} from "@react-pdf/renderer";
import * as jose from "jose";
import fs from "node:fs";

Font.register({
	family: "Roboto Mono",
	src: "https://fonts.gstatic.com/s/robotomono/v11/L0xuDF4xlVMF-BfR8bXMIhJHg45mwgGEFl0_3vq_ROW9.ttf",
});

const isParticipant = (place: number) => place > 10;

const placeToString = (place: number) => {
	return place === 1 ? "1st" : place === 2 ? "2nd" : place === 3 ? "3rd" : `${place}th`;
};

const Certificate = ({
	team,
	place,
	signature,
}: {
	team: string;
	place: number;
	signature: string;
}) => {
	return (
		<Document title={`${team}'s BuckeyeCTF 2023 Certificate`}>
			<Page
				size="A4"
				style={{
					backgroundColor: "black",
					color: "white",
					fontFamily: "Roboto Mono",
				}}
				orientation="landscape"
			>
				<View
					style={{
						position: "absolute",
						display: "flex",
						width: "100%",
						height: "60%",
						justifyContent: "center",
						alignItems: "center",
					}}
				>
					<Image src="buckeyectf-2023-logo.png" style={{ width: 300 }}></Image>
				</View>
				<View
					style={{
						position: "absolute",
						display: "flex",
						width: "100%",
						height: "100%",
					}}
				>
					<Svg>
						{[...Array(100)].map((_, i) => (
							<Circle
								key={i}
								cx={Math.random() * 850}
								cy={Math.random() * 600}
								r={Math.random() * 8 + 1}
								fill="white"
								opacity={Math.random() * 0.6 + 0.2}
							/>
						))}
					</Svg>
				</View>
				<View
					style={{
						position: "absolute",
						display: "flex",
						width: "100%",
						height: "100%",
						justifyContent: "center",
						alignItems: "center",
					}}
				>
					<Text style={{ fontSize: 40 }}>BuckeyeCTF 2023</Text>
				</View>
				<View
					style={{
						position: "absolute",
						display: "flex",
						width: "100%",
						height: "70%",
						justifyContent: "flex-end",
						alignItems: "center",
						fontSize: 25,
					}}
				>
					<Text>Team {team}</Text>
					<Text>
						{isParticipant(place) ? "Participant" : `${placeToString(place)} Place`}
					</Text>
				</View>
				<View>
					<Text style={{ fontSize: 1, color: "black" }}>{signature}</Text>
				</View>
			</Page>
		</Document>
	);
};

// actual solve starts here
const team = "pwned";
const place = 1;
const publicKey = await Bun.file("public_key.pem").text();
const token = await new jose.SignJWT({ team, place })
	.setProtectedHeader({ alg: "HS256" })
	.sign(new TextEncoder().encode(publicKey));

const buffer = await renderToBuffer(<Certificate team={team} place={place} signature={token} />);

fs.writeFileSync("output.pdf", buffer);
