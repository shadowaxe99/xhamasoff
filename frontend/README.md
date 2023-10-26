# Missile Launch Verification Bot - Frontend

This is the frontend for the Missile Launch Verification Bot, an application designed to identify and verify real vs fake missile launches on Twitter in real-time to combat the spread of misinformation.

## Features

1. Real-time updating feed of monitored Twitter data.
2. Statistics dashboard for monitoring bot performance.
3. Interface for manual intervention and auditing.

## Tech Stack

- React.js
- Redux

## Setup

To get the frontend running locally:

- Clone this repository
- `cd` into the `frontend` directory
- Install dependencies with `npm install`
- Start the server with `npm start`

The application will be running at `localhost:3000`.

## Structure

The main components of the frontend are:

- `App.js`: The main component that renders the Dashboard, Feed, and Statistics components.
- `components/Dashboard.js`: Displays the overall statistics of the bot's performance.
- `components/Feed.js`: Displays a real-time feed of the monitored Twitter data.
- `components/Statistics.js`: Displays detailed statistics about the bot's performance.
- `redux/actions.js` and `redux/reducers.js`: Contains the Redux actions and reducers for managing the state of the application.

## Testing

Run `npm test` to run the test suite.

## Deployment

The frontend can be built for production using `npm run build`. This will create a `build` directory with the production-ready code.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)