'use client';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const VotingPage: React.FC = () => {
  const candidates = [
    { id: 1, name: 'Candidate A', party: 'Party X' },
    { id: 2, name: 'Candidate B', party: 'Party Y' },
  ];

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Navbar />
      <main className="flex-grow max-w-4xl mx-auto py-12 px-4">
        <h1 className="text-3xl font-bold mb-8">Cast Your Vote</h1>
        <form className="space-y-6 bg-white p-8 rounded-lg shadow-md">
          {candidates.map((candidate) => (
            <div key={candidate.id} className="flex items-center p-4 border rounded-lg hover:bg-blue-50 transition">
              <input type="radio" id={`candidate-${candidate.id}`} name="candidate" value={candidate.id} className="h-5 w-5 text-blue-600" />
              <label htmlFor={`candidate-${candidate.id}`} className="ml-4">
                <span className="block font-semibold">{candidate.name}</span>
                <span className="text-gray-600">{candidate.party}</span>
              </label>
            </div>
          ))}
          <button type="submit" className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition duration-300">
            Submit Vote
          </button>
        </form>
      </main>
      <Footer />
    </div>
  );
};

export default VotingPage;
