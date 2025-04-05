'use client';
import Link from 'next/link';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <Link href="/" className="text-2xl font-bold text-blue-600">
          VotEase
        </Link>
        <div className="space-x-6">
          <Link href="/voting" className="text-gray-600 hover:text-blue-600">
            Vote
          </Link>
          <Link href="/results" className="text-gray-600 hover:text-blue-600">
            Results
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
