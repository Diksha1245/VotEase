'use client';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-b from-blue-50 to-white">
      <Navbar />
      <main className="flex-grow text-center py-20 px-4">
        <h1 className="text-5xl font-bold text-blue-900 mb-6">Welcome to VotEase</h1>
        <p className="text-xl text-gray-600 mb-8">
          Secure, Accessible, and Modern Voting Platform.
        </p>
        <button className="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition duration-300">
          Get Started
        </button>
      </main>
      <Footer />
    </div>
  );
};

export default HomePage;
