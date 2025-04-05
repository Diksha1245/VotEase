'use client';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';

const ResultsPage: React.FC = () => {
  const data = {
    labels: ['Candidate A', 'Candidate B'],
    datasets: [
      {
        label: 'Votes',
        data: [65, 35],
        backgroundColor: ['#2563eb', '#1d4ed8'],
      },
    ],
  };

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Navbar />
      <main className="flex-grow max-w-4xl mx-auto py-12 px-4">
        <h1 className="text-3xl font-bold mb-8">Live Results</h1>
        <div className="bg-white p-8 rounded-lg shadow-md h-[400px]">
          <Bar data={data} options={{ maintainAspectRatio: false }} />
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default ResultsPage;
