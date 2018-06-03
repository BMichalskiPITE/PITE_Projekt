import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Dashboard',
    icon: 'nb-home',
    link: '/dashboard',
    home: true,
  },
  {
    title: 'Tourist',
    icon: 'nb-location',
    data: {
      permission: [
        'tourist'
      ],
    },
    children: [
      {
        title: 'Your trips',
        icon: 'nb-location',
        link: '/tourist/trips',
        data: {
          permission: [
            'tourist'
          ],
        }
      },
      {
        title: 'Add new trip',
        icon: 'nb-location',
        link: '/tourist/trip',
        data: {
          permission: [
            'tourist'
          ],
        }
      }
    ]
  },
  {
    title: 'Guide',
    icon: 'nb-location',
    data: {
      permission: [
        'guide'
      ],
    },
    children: [
      {
        title: 'Find trips',
        icon: 'nb-location',
        link: '/guide/find',
        data: {
          permission: [
            'guide'
          ],
        }
      },
      {
        title: 'Your trips',
        icon: 'nb-location',
        link: '/guide/trips',
        data: {
          permission: [
            'guide'
          ],
        }
      }
    ]
  },
  {
    title: 'Messages',
    icon: 'nb-email',
    link: '/messages'
  }
];
